import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com')


@pytest.fixture(scope='function')
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(10)
    browser.set_window_size(1400, 1000)
    yield browser
    browser.close()
