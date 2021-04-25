import json
import logging
import os
from datetime import datetime
from urllib.parse import urljoin

import requests

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
        response = self.session.request(method, url, headers=headers, data=data, allow_redirects=allow_redirects,
                                        files=files)
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
        location = '/csrf'
        headers = {'Cookie': f'mc={self.session.cookies["mc"]}'}
        new_headers = self._request('GET', location=location, jsonify=False, headers=headers).headers[
            'Set-Cookie'].split(';')
        token_header = [h for h in new_headers if 'csrftoken' in h]
        if not token_header:
            raise Exception('CSRF token not found in main page headers')

        token = self.session.cookies['csrftoken']
        return token

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
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        result = self._request('POST', location, headers=headers, data=data, jsonify=False)

        self.base_url = 'https://target.my.com'
        csrftoken = self.get_token()

        return result

    def post_image(self):
        location = "api/v2/content/static.json"
        headers = {
            'Cookie': f'mc={self.session.cookies["mc"]}; csrftoken={self.session.cookies["csrftoken"]}; sdcs={self.session.cookies["sdcs"]}',
            'X-CSRFToken': f'{self.session.cookies["csrftoken"]}'}

        new_img = open(self.get_image('test.jpg'), mode='rb')

        files = {'file': ('test.jpg', new_img, 'image/jpeg')}

        result = self._request('POST', location, headers=headers, files=files)
        return result

    def post_campaign_create(self):
        location = "/api/v2/campaigns.json"
        headers = self.post_headers
        headers['Content-Type'] = "application/json"
        headers[
            'Cookie'] = f'mc={self.session.cookies["mc"]}; csrftoken={self.session.cookies["csrftoken"]}; sdcs={self.session.cookies["sdcs"]}'
        headers['X-CSRFToken'] = f'{self.session.cookies["csrftoken"]}'

        current_date = datetime.now()
        campaign_title = f"TestCampaignAPI at {current_date}"
        json_campaign = self.get_json_file('campaign.json')

        img_id = self.post_image()['id']
        json_campaign['name'] = campaign_title
        json_campaign['banners'][0]['urls']['primary']['id'] = img_id
        json_campaign['banners'][0]['content']['image_90x75']['id'] = img_id
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
            'status': 'deleted'
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
