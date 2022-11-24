import pytest
from selene.support.shared import browser
from selene import be


@pytest.fixture(scope="session")
def open_browser():
    browser.config.window_width = 1400
    browser.config.window_height = 800
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
