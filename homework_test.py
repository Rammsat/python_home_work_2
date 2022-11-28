from selene.support.shared import browser
from selene import have, be


def test_positive(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in'))


def test_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('gdfjkgdjflkglkdfjg').press_enter()
    assert browser.element('[id="topstuff"]').should(have.text('По запросу gdfjkgdjflkglkdfjg ничего не найдено.'))
