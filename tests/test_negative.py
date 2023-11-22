from pages.endpoints import EndPoints
from pages.item_page import ItemPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ItemPage(browser, EndPoints.ITEM_PAGE)
    page.open()
    page.add_item_into_basket()
    page.should_not_add_alert()

def test_guest_cant_see_success_message(browser):
    page = ItemPage(browser, EndPoints.ITEM_PAGE)
    page.open()
    page.should_not_add_alert()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ItemPage(browser, EndPoints.ITEM_PAGE)
    page.open()
    page.add_item_into_basket()
    page.should_add_alert_disappear()