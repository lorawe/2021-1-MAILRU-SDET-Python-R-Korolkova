from datetime import datetime

import allure

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import SegmentsPageLocators


class SegmentsPage(BasePage):
    url = "https://target.my.com/segments/segments_list"
    locators = SegmentsPageLocators()

    @allure.step('Create segment')
    def create_segment(self):
        try:
            self.click(self.locators.CREATE_SEGMENT_BUTTON)
        except:
            self.click(self.locators.SUBMIT_BUTTON_CREATE)
        self.click(self.locators.SEGMENT_APPS)
        self.click(self.locators.SEGMENT_APPS_CHECKBOX)
        self.click(self.locators.SUBMIT_BUTTON_ADD)
        current_date = datetime.now()
        segment_title = f"TestSegment at {current_date}"
        self.send(segment_title, self.locators.INPUT_SEGMENT_TITLE)
        self.click(self.locators.SUBMIT_BUTTON_CREATE)
        return segment_title

    @allure.step('Delete last segment')
    def delete_segment(self):
        self.click(self.locators.REMOVE_BUTTON)
        self.click(self.locators.BUTTON_CONFIRM_REMOVE)

    @allure.step('Check segment {title}')
    def check_segment(self, title):
        title_locator = (self.locators.SEGMENT_TABLE_TITLE[0],
                         self.locators.SEGMENT_TABLE_TITLE[1].format(title))
        assert self.find(title_locator)

    @allure.step('Check deleted segment {title}')
    def check_deleted_segment(self, title):
        title_locator = (self.locators.SEGMENT_TABLE_TITLE[0],
                         self.locators.SEGMENT_TABLE_TITLE[1].format(title))

        self.wait_missing(title_locator)

