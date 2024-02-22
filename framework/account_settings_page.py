from .page import Page
from selenium.webdriver.common.by import By


class AccountSettingsPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.logout_button = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]")

    def logout_account(self):
        self.click_element(*self.logout_button)


