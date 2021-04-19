import base64
import json
import logging
import os
from datetime import datetime
from urllib.parse import urljoin

import requests
from requests.cookies import cookiejar_from_dict

logger = logging.getLogger('test')

MAX_RESPONSE_LENGTH = 500


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class InvalidLoginException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

        self.csrf_token = None
        self.sessionid_gtp = None

    @staticmethod
    def log_pre(method, url, headers, data, expected_status):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = 'Got response:\n' \
                  'RESPONSE STATUS: {response.status_code}'

        if len(response.text) > MAX_RESPONSE_LENGTH:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n\n')
            elif logger.level == logging.DEBUG:
                logger.debug(f'{log_str}\n'
                             f'RESPONSE CONTENT: {response.text}\n\n')
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n')

    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=True,
                 allow_redirects=True, files=None):
        url = urljoin(self.base_url, location)

        self.log_pre(method, url, headers, data, expected_status)
        response = self.session.request(method, url, headers=headers, data=data, allow_redirects=allow_redirects, files=files)
        self.log_post(response)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"!\n'
                                              f'Expected status_code: {expected_status}.')

        if jsonify:
            json_response = response.json()
            if json_response.get('bStateError'):
                error = json_response.get('bErrorMsg', 'Unknown')
                raise ResponseErrorException(f'Request "{url}" return error "{error}"!')
            return json_response
        return response

    @property
    def post_headers(self):
        return {'Content-Type': 'application/x-www-form-urlencoded'}

    def get_token(self):
        headers = self.post_headers
        headers['Cookie'] = f'mc={self.session.cookies["mc"]}; ssdc={self.session.cookies["ssdc"]}; sdcs={self.session.cookies["sdcs"]}'
        new_headers = self._request('GET', urljoin(self.base_url, '/csrf'), jsonify=False, headers=headers).headers['Set-Cookie'].split(';')
        token_header = [h for h in new_headers if 'csrftoken' in h]
        if not token_header:
            raise Exception('CSRF token not found in main page headers')

        token_header = token_header[0]
        token = token_header.split('=')[-1]

        return token

    def get_sdcs(self, url):
        self.base_url = url
        location = ''
        headers = self.post_headers
        headers['Cookies'] = f'mc={self.session.cookies["mc"]}'

        result = self._request('GET', location, headers=headers, expected_status=302,
                               allow_redirects=False, jsonify=False)

        try:
            response_cookies = result.headers['Set-Cookie'].split(';')
        except Exception as e:
            raise InvalidLoginException(e)

        new_sdcs = [c for c in response_cookies if "sdcs" in c][0].split('=')[-1]
        return new_sdcs

    def get_sdcs_token(self, url):
        location = url
        headers = self.post_headers
        headers['Cookies'] = f'mc={self.session.cookies["mc"]}'

        result = self._request('GET', location, headers=headers, expected_status=302,
                               allow_redirects=False, jsonify=False)
        try:
            response_location = result.headers['Location']
        except Exception as e:
            raise InvalidLoginException(e)

        return response_location

    def get_json_file(self, filename):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, f'../resources/{filename}')
        file = os.path.normpath(file_path)
        with open(file, encoding='utf-8') as f:
            json_file = json.load(f)
        return json_file

    def get_image(self, filename):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, f'../resources/{filename}')
        file = os.path.normpath(file_path)
        return file

    def post_login(self, user, password):
        self.base_url = 'https://auth-ac.my.com'
        location = '/auth'

        headers = self.post_headers
        headers['Referer'] = 'https://target.my.com/'
        headers['Origin'] = 'https://target.my.com'

        data = {
            'email': user,
            'password': password,
        }

        result = self._request('POST', location, headers=headers, data=data, jsonify=False, expected_status=302,
                               allow_redirects=False)

        try:
            response_cookies = result.headers['Set-Cookie'].split(';')
        except Exception as e:
            raise InvalidLoginException(e)

        new_location = '/sdc?from=https%3A%2F%2Ftarget.my.com%2Fauth%2Fmycom%3Fstate%3Dtarget_login%253D1%2526ignore_opener%253D1'
        new_sdcs_token_location = self.get_sdcs_token(new_location)

        sdcs_url = new_sdcs_token_location
        new_sdcs = self.get_sdcs(url=sdcs_url)

        self.base_url = 'https://target.my.com'
        csrftoken = self.get_token()

        return result

    def post_image(self):
        location = "api/v2/content/static.json"
        headers = self.post_headers
        headers['Content-Type'] = "multipart/form-data; boundary=----WebKitFormBoundaryzV0dcU6bUOexnUAW"
        headers[
            'Cookie'] = f'mc={self.session.cookies["mc"]}; csrftoken={self.session.cookies["csrftoken"]}; sdcs={self.session.cookies["sdcs"]}'
        headers['X-CSRFToken'] = f'{self.session.cookies["csrftoken"]}'

        new_img = open(self.get_image('test.jpg'), mode='rb')

        files = [
            ('file', ('test.jpg', new_img, 'image/jpeg')),
            ('data', '{"width":0,"height":0}')]

        result = self._request('POST', location, headers=headers, files=files)
        return result


    def post_campaign_create(self):
        location = "/api/v2/campaigns.json"
        headers = self.post_headers
        headers['Content-Type'] = "application/json"
        headers['Cookie'] = f'mc={self.session.cookies["mc"]}; csrftoken={self.session.cookies["csrftoken"]}; sdcs={self.session.cookies["sdcs"]}'
        headers['X-CSRFToken'] = f'{self.session.cookies["csrftoken"]}'

        current_date = datetime.now()
        campaign_title = f"TestCampaignAPI at {current_date}"
        json_campaign = self.get_json_file('campaign.json')
        json_campaign['name'] = campaign_title

        data = json.dumps(json_campaign)

        result = self._request('POST', location, headers=headers, data=data)
        return result

    def delete_campaign(self, campaign_id):
        location = f'/api/v2/campaigns/{campaign_id}.json'
        headers = self.post_headers
        headers['Content-Type'] = "application/json"
        headers[
            'Cookie'] = f'mc={self.session.cookies["mc"]}; csrftoken={self.session.cookies["csrftoken"]}; sdcs={self.session.cookies["sdcs"]}'
        headers['X-CSRFToken'] = f'{self.session.cookies["csrftoken"]}'

        data = {
            'status':'deleted'
        }

        data = json.dumps(data)

        result = self._request('POST', location, headers=headers, data=data, expected_status=204, jsonify=False)
        return result

    def post_segment_create(self):
        location = "/api/v2/remarketing/segments.json"
        headers = self.post_headers
        headers['Content-Type'] = "application/json"
        headers[
            'Cookie'] = f'mc={self.session.cookies["mc"]}; csrftoken={self.session.cookies["csrftoken"]}; sdcs={self.session.cookies["sdcs"]}'
        headers['X-CSRFToken'] = f'{self.session.cookies["csrftoken"]}'

        current_date = datetime.now()
        segment_title = f"TestSegmentAPI at {current_date}"
        json_segment = self.get_json_file('segment.json')
        json_segment['name'] = segment_title

        data = json.dumps(json_segment)

        result = self._request('POST', location, headers=headers, data=data)
        return result

    def post_segment_delete(self, segment_id):
        location = "/api/v1/remarketing/mass_action/delete.json"
        headers = self.post_headers
        headers['Content-Type'] = "application/json"
        headers[
            'Cookie'] = f'mc={self.session.cookies["mc"]}; csrftoken={self.session.cookies["csrftoken"]}; sdcs={self.session.cookies["sdcs"]}'
        headers['X-CSRFToken'] = f'{self.session.cookies["csrftoken"]}'

        data = [
            {'source_id': f'{segment_id}',
                       'source_type': 'segment'
             }
        ]

        data = json.dumps(data)

        result = self._request('POST', location, headers=headers, data=data, jsonify=True)
        return result

    def check_segment(self, segment_id, is_exist=True):
        location = f'/api/v2/remarketing/segments/{segment_id}.json'
        headers = self.post_headers
        headers['Content-Type'] = "application/json"
        headers[
            'Cookie'] = f'mc={self.session.cookies["mc"]}; csrftoken={self.session.cookies["csrftoken"]}; sdcs={self.session.cookies["sdcs"]}'
        headers['X-CSRFToken'] = f'{self.session.cookies["csrftoken"]}'
        if is_exist:
            result = self._request('GET', location, headers=headers, expected_status=200)
        else:
            result = self._request('GET', location, headers=headers, expected_status=404)
        return result