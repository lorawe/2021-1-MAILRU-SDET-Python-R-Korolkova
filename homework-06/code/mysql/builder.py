from random import random

from mysql.models import BadRequest, ServerErrorRequest, CountMethod, CountRequest, TopRequest


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_count_request(self, count):
        if count is None:
            count = random.randint(0, 1000)

        count_request = CountRequest(
            count=count
        )
        self.client.session.add(count_request)
        return count_request

    def create_count_method(self, method, count):
        if count is None:
            count = random.randint(0, 1000)

        if method is None:
            method = 'GET'

        count_method = CountMethod(
            count=count,
            method=method,
        )
        self.client.session.add(count_method)
        return count_method

    def create_top_request(self, url, count):
        if count is None:
            count = random.randint(0, 1000)

        if url is None:
            url = f'https://mail.ru/'

        top_request = TopRequest(
            count=count,
            url=url
        )
        self.client.session.add(top_request)
        return top_request

    def create_bad_request(self, url, status, weight, ip):
        if url is None:
            url = f'https://mail.ru/'

        if status is None:
            status = '404'

        if weight is None:
            weight = random.randint(0, 1000)

        if ip is None:
            ip = f'127.0.0.{random.randint(0, 255)}'

        bad_request = BadRequest(
            url=url,
            status=status,
            weight=weight,
            ip=ip
        )
        self.client.session.add(bad_request)
        return bad_request

    def create_server_err_request(self, count, ip):
        if count is None:
            count = random.randint(0, 1000)

        if ip is None:
            ip = f'127.0.0.{random.randint(0, 255)}'

        server_err_request = ServerErrorRequest(
            count=count,
            ip=ip
        )
        self.client.session.add(server_err_request)
        return server_err_request
