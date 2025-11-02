from selene import browser, be, have
from allure import step

class FilterPage:
    def open(self):
        browser.open('/ruza/')
        return self

    def fill_search(self, query):
        browser.element('input[placeholder*="Поиск"]').should(be.visible).set_value(query).press_enter()
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

class Realty_Page:

    def realty_open(self):
        browser.open('/ruza/realty/sale')
        return self


    def realty_price_button(self, min_price=180, max_price=500):
        browser.element('input._tupxg39').should(be.visible).clear().type(str(min_price)).press_enter()
        browser.element('input._1kvvnrkq').should(be.visible).clear().type(str(max_price)).press_enter()
        return self



    def realty_should_be_loaded(self):
        browser.element('h1, h2').should(have.text('Продажа недвижимости'))
        browser.element('button, [role="button"], a').with_(timeout=10).should(have.text('Фильтры'))
        return self

    def realty_search(self, query, min_price=1800000, max_price=5000000):
        browser.open('https://2gis.ru/ruza/realty/sale')
        browser.element('input[placeholder*="Район, улица, дом..."]').should(be.visible).set_value(query).press_enter()
        browser.element('input._1qyj3m0').should(be.visible).clear().type(str(min_price)).press_enter()
        browser.element('input._1qyj3m0').should(be.visible).clear().type(str(max_price)).press_enter()
        return self
