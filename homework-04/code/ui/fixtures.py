import os
import shutil

import allure
import pytest
from appium import webdriver
from selenium import webdriver as wd
from ui.pages.base_page import BasePage

from ui import pages

from ui.capability import capability_select


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    page = get_page('MainPage')
    return page(driver=driver, config=config)


@pytest.fixture
def settings_page(driver, config):
    page = get_page('SettingsPage')
    return page(driver=driver, config=config)


@pytest.fixture
def search_page(driver, config):
    page = get_page('SearchPage')
    return page(driver=driver, config=config)

@pytest.fixture
def about_page(driver, config):
    page = get_page('AboutPage')
    return page(driver=driver, config=config)


def get_page(page_class):
    page_class += 'ANDROID'
    page = getattr(pages, page_class, None)
    if page is None:
        raise Exception(f'No such page {page_class}')
    return page


def get_driver(appium_url):
    desired_caps = capability_select()
    driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
    return driver


@pytest.fixture(scope='function')
def driver(config, test_dir):
    appium_url = config['appium']
    browser = get_driver(appium_url)
    yield browser
    browser.quit()
