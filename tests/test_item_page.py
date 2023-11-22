from pages.item_page import ItemPage
from pages.endpoints import *


def test_guest_can_add_product_to_basket(browser):
    item_page = ItemPage(browser, EndPoints.ITEM_PAGE)
    item_page.open()
    item_page.add_item_into_basket()
    item_page.solve_quiz_and_get_code()
    item_page.should_item_added()


def test_guest_can_add_other_product_to_basket(browser):
    item_page = ItemPage(browser, EndPoints.NEW_ITEM_PAGE)
    item_page.open()
    item_page.add_item_into_basket()
    item_page.solve_quiz_and_get_code()
    item_page.should_item_added()
