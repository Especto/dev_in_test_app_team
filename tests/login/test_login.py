import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("email, password, expected_result", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
    ("qa.ajax.app.automation@gmail.co", "qa_automation_password", False),
    ("qa.ajax.app.automation@gmail.com", "qa_automation_passwor", False),
])
def test_user_login(user_login_fixture, email, password, expected_result):
    login_page = user_login_fixture
    logger.info("Starting activity")
    login_page.open_page()
    logger.info("Opening the login page")

    login_page.enter_email(email)
    logger.info(f"Email {email} entered")
    login_page.enter_password(password)
    logger.info(f"Password {password} entered")
    login_page.click_login_button()
    logger.info("Clicked login button")

    if expected_result:
        logger.info("Authorized")
        assert login_page.is_authorized(), "Positive case failed"
        login_page.logout_from_account()
        logger.info("Account logout is successful")
    else:
        assert not login_page.is_authorized(), "Negative case failed"
        logger.info("Not authorized")
        login_page.go_back()
        logger.info("Return to start page")
