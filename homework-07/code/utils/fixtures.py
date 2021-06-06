import pytest
import json

import settings
from client.http_client import HttpClient


@pytest.fixture(scope='function')
def http_client():
    http_client = HttpClient()
    http_client.connect()
    yield http_client
    http_client.close()

@pytest.fixture(scope='function')
def create_user(http_client):
    name = 'Egor'
    params_old = f'{name}/Pupin'
    result = http_client.post(params_old)
    http_client.close()
    return result
