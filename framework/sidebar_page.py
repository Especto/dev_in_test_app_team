from .account_settings_page import AccountSettingsPage
from .page import Page
from selenium.webdriver.common.by import By


class SidebarPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.settings_button = (By.ID, "com.ajaxsystems:id/settings")
        self.help_button = (By.ID, "com.ajaxsystems:id/help")
        self.logs_button = (By.ID, "com.ajaxsystems:id/logs")
        self.camera_button = (By.ID, "com.ajaxsystems:id/camera")
        self.add_hub_button = (By.ID, "com.ajaxsystems:id/addHub")
        self.doc_button = (By.ID, "com.ajaxsystems:id/documentation_text")

    def open_settings_page(self) -> AccountSettingsPage:
        self.click_element(*self.settings_button)
        return AccountSettingsPage(self.driver)

    def open_help_page(self):
        self.click_element(*self.help_button)

    def open_logs_page(self):
        self.click_element(*self.logs_button)

    def open_camera(self):
        self.click_element(*self.camera_button)

    def is_settings_button_visible(self):
        return self.is_element_visible(*self.settings_button)

    def is_help_button_visible(self):
        return self.is_element_visible(*self.help_button)

    def is_logs_button_visible(self):
        return self.is_element_visible(*self.logs_button)

    def is_camera_button_visible(self):
        return self.is_element_visible(*self.camera_button)

    def is_add_hub_button_visible(self):
        return self.is_element_visible(*self.add_hub_button)

    def is_doc_button_visible(self):
        return self.is_element_visible(*self.doc_button)

    def is_settings_button_enabled(self):
        return self.is_element_enabled(*self.settings_button)

    def is_help_button_enabled(self):
        return self.is_element_enabled(*self.help_button)

    def is_logs_button_enabled(self):
        return self.is_element_enabled(*self.logs_button)

    def is_camera_button_enabled(self):
        return self.is_element_enabled(*self.camera_button)

    def is_add_hub_button_enabled(self):
        return self.is_element_enabled(*self.add_hub_button)

    def is_doc_button_enabled(self):
        return self.is_element_enabled(*self.doc_button)

    def logout_from_account(self):
        account_settings_page = self.open_settings_page()
        account_settings_page.logout_account()




