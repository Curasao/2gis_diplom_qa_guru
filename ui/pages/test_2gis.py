from selene import browser, be, have, command
from allure import step

class FilterPage:
    def open(self):
        browser.open('/ruza/search/')
        browser.execute_script('window.scrollBy(0, 500)')
        return self

    def fill_search(self,query):
        browser.element('input[placeholder="Поиск в 2ГИС"]').should(be.blank).type(query).press_enter()
        return self

    def dostavka_button(self):
        browser.element('label._w9ask7').click()
        return self

    def rate_button(self):
        browser.element('label._1btz1t0f').click()
        return self

    def price_button(self, min_price=180, max_price=500):
        browser.element('input._tupxg39').should(be.visible).clear().type(str(min_price))
        browser.element('input._1kvvnrkq').should(be.visible).clear().type(str(max_price)).press_enter()
        return self
