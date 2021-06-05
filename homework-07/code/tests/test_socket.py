import json

import settings
from client.http_client import HttpClient
from tests.test import BaseCase
from utils.fixtures import *


class Tests(BaseCase):

    def test_post(self, http_client):
        params = 'Egor/Postin'
        name = 'Egor'
        post_result = http_client.post(params)
        result = http_client.get(name)
        assert json.loads(result[-1]) == ['Egor', 'Postin']

    def test_put(self, http_client, create_user):
        name = 'Egor'
        params = 'Egor/Testovich'
        user = create_user
        print(user)
        result = http_client.put(params)
        #result = http_client.get(name)
        assert json.loads(result[-1]) == ['Egor', 'Pupin']

    def test_delete(self, http_client, create_user):
        name = 'Egor'
        result = http_client.delete(name)
        #result = http_client.get(name)
        assert json.loads(result[-1]) == ['Egor', 'Pupin']
