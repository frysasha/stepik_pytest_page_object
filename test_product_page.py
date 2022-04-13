from time import sleep
from .pages.product_page import ProductPage
import pytest


class TestUserAddToBasketFromProductPage:

    def test_guest_cant_see_success_message(self, browser):


    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                             pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                          marks=pytest.mark.xfail)])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_correct_prise()
        page.should_be_correct_name()

