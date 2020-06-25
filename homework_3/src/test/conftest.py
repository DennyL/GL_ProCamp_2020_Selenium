import pytest
from homework_3.src.test.config import Browser


@pytest.fixture(scope='session')
def browser():
    browser = Browser(with_browser='Chrome')
    yield browser.driver
    browser.destroy_and_quit()
