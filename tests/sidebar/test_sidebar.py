import logging
import pytest

from framework.main_page import MainPage


logger = logging.getLogger(__name__)


def check_element_visibility_and_clickability(sidebar_page, element_name):
    assert getattr(sidebar_page, f'is_{element_name}_button_visible')(), f"{element_name} button is not visible"
    assert getattr(sidebar_page, f'is_{element_name}_button_enabled')(), f"{element_name} button is not enabled"
    logger.info(f"{element_name} button is visible and clickable")


@pytest.mark.usefixtures("sidebar_fixture")
def test_sidebar_elements(sidebar_fixture):
    login_page = sidebar_fixture
    logger.info("Starting activity")
    login_page.open_page()
    logger.info("Opening the login page")

    login_page.enter_email("qa.ajax.app.automation@gmail.com")
    logger.info("Email entered")
    login_page.enter_password("qa_automation_password")
    logger.info("Password entered")
    login_page.click_login_button()
    logger.info("Clicked login button")

    assert login_page.is_authorized(), "Authorization failed"
    logger.info("Authorized")

    main_page = MainPage(login_page.driver)
    sidebar_page = main_page.open_sidebar_page()

    check_element_visibility_and_clickability(sidebar_page, 'settings')
    check_element_visibility_and_clickability(sidebar_page, 'help')
    check_element_visibility_and_clickability(sidebar_page, 'logs')
    check_element_visibility_and_clickability(sidebar_page, 'camera')
    check_element_visibility_and_clickability(sidebar_page, 'add_hub')
    check_element_visibility_and_clickability(sidebar_page, 'doc')

    '''assert sidebar_page.is_settings_button_visible(), "Settings button is not visible"
    assert sidebar_page.is_help_button_visible(), "Help button is not visible"
    assert sidebar_page.is_logs_button_visible(), "Logs button is not visible"
    assert sidebar_page.is_camera_button_visible(), "Camera button is not visible"
    assert sidebar_page.is_add_hub_button_visible(), "Add Hub button is not visible"
    assert sidebar_page.is_doc_button_visible(), "Documentation button is not visible"

    assert sidebar_page.is_settings_button_clickable(), "Settings button is not clickable"
    assert sidebar_page.is_help_button_clickable(), "Help button is not clickable"
    assert sidebar_page.is_logs_button_clickable(), "Logs button is not clickable"
    assert sidebar_page.is_camera_button_clickable(), "Camera button is not clickable"
    assert sidebar_page.is_add_hub_button_clickable(), "Add Hub button is not clickable"
    assert sidebar_page.is_doc_button_clickable(), "Documentation button is not clickable"'''

    logger.info("All elements have been checked")
    sidebar_page.logout_from_account()
    logger.info("Account logout is successful")

