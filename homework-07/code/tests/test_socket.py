import json

import settings
from client.http_client import HttpClient
from tests.test import BaseCase
from utils.fixtures import *


class TestMock(BaseCase):

    def test_post(self, http_client):
        params = 'Egor/Postin'
        name = 'Egor'
        post_result = http_client.post(params)
        result = http_client.get(name)
        assert json.loads(result[-1]) == {'Egor': 'Postin'}

    def test_put(self, create_user):
        name = 'Egor'
        params = 'Egor/Testovich'
        user = create_user
        http_client = HttpClient()
        http_client.connect()
        put_result = http_client.put(params)
        result = http_client.get(name)
        http_client.close()
        assert json.loads(result[-1]) == {'Egor': 'Testovich'}

    def test_delete(self, create_user):
        name = 'Egor'
        http_client = HttpClient()
        http_client.connect()
        http_client.delete(name)
        result = http_client.get(name)
        http_client.close()
        assert json.loads(result[-1]) == 'Egor'
