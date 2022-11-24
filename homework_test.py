from selene.support.shared import browser
from selene import have


def test_positive(open_browser):
    assert browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in'))


def test_negative(open_browser):
    assert browser.element('[id="search"]').should(have.text('qwe'))
