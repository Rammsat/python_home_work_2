import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function")
def open_browser():
    browser.config.window_width = 1400
    browser.config.window_height = 800
    browser.open('https://google.com')
