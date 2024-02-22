
from .account_settings_page import AccountSettingsPage
from .main_page import MainPage
from .page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from .sidebar_page import SidebarPage


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.start_button = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.Button")
        self.back_button = (By.ID, "com.ajaxsystems:id/back")
        self.login_button = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.Button")
        self.email_field = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
        self.password_field = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
        self.unauthorized_message = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]")

    def open_page(self):
        self.click_element(*self.start_button)

    def enter_email(self, username):
        self.send_keys(*self.email_field, username)

    def enter_password(self, password):
        self.send_keys(*self.password_field, password)

    def click_login_button(self):
        self.click_element(*self.login_button)

    def is_authorized(self):
        try:
            self.find_element(*self.unauthorized_message)  # search for failed authorization message
            return False
        except NoSuchElementException:
            return True

    def logout_from_account(self):
        sidebar_page = MainPage(self.driver).open_sidebar_page()
        account_settings_page = sidebar_page.open_settings_page()
        account_settings_page.logout_account()

    def go_back(self):
        self.click_element(*self.back_button)
