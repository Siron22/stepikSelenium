from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.endpoints import *


def test_guest_can_add_product_to_basket(browser):
    item_page = ProductPage(browser, EndPoints.PRODUCT_PAGE)
    item_page.open()
    item_page.add_item_into_basket()
    item_page.solve_quiz_and_get_code()
    item_page.should_item_added()


def test_guest_can_add_other_product_to_basket(browser):
    item_page = ProductPage(browser, EndPoints.NEW_PRODUCT_PAGE)
    item_page.open()
    item_page.add_item_into_basket()
    item_page.solve_quiz_and_get_code()
    item_page.should_item_added()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, EndPoints.CITY_STARS)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, EndPoints.CITY_STARS)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
