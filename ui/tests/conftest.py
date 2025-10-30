import inspect
import pytest
from selene import browser

@pytest.fixture(scope='function')
def setup_browser():


    # Базовые настройки Selene
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://2gis.ru'
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.type_by_js = False
    browser.config.hold_browser_open = False
    yield browser

    browser.quit()