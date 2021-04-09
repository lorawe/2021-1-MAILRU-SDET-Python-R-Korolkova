import allure

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import CampaignPageLocators




class CampaignPage(BasePage):
    url = 'https://target.my.com/campaign/new'
    locators = CampaignPageLocators()

    @allure.step('Creating campaign')
    def create_campaign(self):
        self.click(self.locators.TRAFFIC)
        self.send(self.locators.AD_URL, self.locators.INPUT_LINK)
        self.click(self.locators.TEASER)
        self.send_file(self.locators.FILE, self.locators.INPUT_FILE)
        self.send(self.locators.TITLE, self.locators.INPUT_TITLE)
        self.send(self.locators.TEXT, self.locators.INPUT_TEXT)
        self.click(self.locators.SUBMIT_BUTTON)
