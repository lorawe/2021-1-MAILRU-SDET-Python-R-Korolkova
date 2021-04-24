import allure
import random

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import CampaignPageLocators




class CampaignPage(BasePage):
    url = 'https://target.my.com/campaign/new'
    file_jpg = 'test.jpg'
    locators = CampaignPageLocators()

    @allure.step('Creating campaign')
    def create_campaign(self):
        random_value = random.randint(0, 10)
        ad_url = f'TestCampaignUrl{random_value}.ru'
        ad_title = f'TestCampaignTitle{random_value}'
        ad_text = f'TestCampaigText{random_value}'
        self.click(self.locators.TRAFFIC)
        self.send(ad_url, self.locators.INPUT_LINK)
        self.click(self.locators.TEASER)
        self.send_file(self.file_jpg, self.locators.INPUT_FILE)
        self.send(ad_title, self.locators.INPUT_TITLE)
        self.send(ad_text, self.locators.INPUT_TEXT)
        self.click(self.locators.SUBMIT_BUTTON)
