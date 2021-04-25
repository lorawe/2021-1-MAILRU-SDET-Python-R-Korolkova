import allure
import random
from datetime import datetime

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import CampaignPageLocators




class CampaignPage(BasePage):
    url = 'https://target.my.com/campaign/new'
    file_jpg = 'test.jpg'
    locators = CampaignPageLocators()

    @allure.step('Creating campaign')
    def create_campaign(self):
        random_value = random.randint(0, 100)
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        ad_url = f'TestUrl{random_value}.ru'
        ad_title = f'Test{current_time}'
        ad_text = f'TestText{current_time}'
        self.click(self.locators.TRAFFIC)
        self.send(ad_url, self.locators.INPUT_LINK)
        self.click(self.locators.TEASER)
        self.send_file(self.file_jpg, self.locators.INPUT_FILE)
        self.send(ad_title, self.locators.INPUT_TITLE)
        self.send(ad_text, self.locators.INPUT_TEXT)
        self.send(ad_title, self.locators.INPUT_CAMPAIGN_TITLE)
        self.click(self.locators.SUBMIT_BUTTON)
        return ad_title
