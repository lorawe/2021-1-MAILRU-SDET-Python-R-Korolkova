import allure
import pytest

from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.pages.segments_page import SegmentsPage
from ui.locators.pages_locators import DashboardPageLocators


class DashboardPage(BasePage):
    url = 'https://target.my.com/dashboard'
    locators = DashboardPageLocators()

    @allure.step('Going to segments')
    def go_to_segments(self):
        page_locator = ((self.locators.PAGE_LOCATORS_TEMPLATE[0],
                         self.locators.PAGE_LOCATORS_TEMPLATE[1].format('segments')))
        self.click(page_locator)
        return SegmentsPage(self.driver)

    @allure.step('Going to campaign')
    def go_to_campaign(self):
        try:
            self.click(self.locators.CAMPAIGN_NEW)
        except Exception:
            self.click(self.locators.CAMPAIGN_NEW_2)
        return CampaignPage(self.driver)

    @allure.step('Check campaign')
    def check_campaign(self, campaign_title):
        capmaign_locator = ((self.locators.CAMPAIGN_TITLE_TEMPLATE[0],
                         self.locators.CAMPAIGN_TITLE_TEMPLATE[1].format(campaign_title)))
        assert (self.find(capmaign_locator), "Новая компания не найдена")


    @allure.step('Delete campaign')
    def delete_campaign(self):
        with pytest.raises(Exception):
            self.click(self.locators.SETTING_CAMPAIGN)
            self.click(self.locators.DELETE_LI)
            self.click(self.locators.CAMPAIGN_CHECKBOX)

