from ui.pages.test_2gis import Realty_Page
from ui.pages.test_2gis import FilterPage

def test_form_submission(setup_browser_filter):
    filter_page = FilterPage()

    # Открываем страницу
    filter_page.open()
    filter_page.fill_search("Кофейни")
    filter_page.dostavka_button()
    filter_page.rate_button()
    filter_page.price_button()


def test_realty_search(setup_browser_realty):
    realty_page = Realty_Page()
    realty_page.realty_search("Тучково")


def test_realty_filters_price_and_rooms(setup_browser_realty):
    realty_page = Realty_Page()
    realty_page.realty_open()
    realty_page.realty_price_button(400, 800)  # Пример установки цены





    

