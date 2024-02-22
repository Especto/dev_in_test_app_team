import pytest
from framework import LoginPage


@pytest.fixture(scope='function')
def sidebar_fixture(driver):
    yield LoginPage(driver)
