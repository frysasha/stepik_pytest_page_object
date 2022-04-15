from . base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Basket in not empty'

    def should_be_not_content_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CONTENT_IN_BASKET), \
                                                        'Content in basket, but should not be'
