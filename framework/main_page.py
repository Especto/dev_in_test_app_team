from .page import Page
from selenium.webdriver.common.by import By
from .sidebar_page import SidebarPage


class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.sidebar_button = (By.ID, "com.ajaxsystems:id/menuDrawer")

    def open_sidebar_page(self) -> SidebarPage:
        self.click_element(*self.sidebar_button)
        return SidebarPage(self.driver)
