from ui.pages.test_2gis import FilterPage


def test_form_submission(setup_browser):
    registration_page = FilterPage()

    # Открываем страницу
    registration_page.open()
    registration_page.fill_search("Кофейни")
    registration_page.dostavka_button()
    registration_page.rate_button()

