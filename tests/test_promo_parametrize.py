import time
import pytest
from pages.endpoints import EndPoints
from pages.item_page import ItemPage


@pytest.mark.parametrize('link', EndPoints.PROMO_LINKS)
def test_guest_can_add_product_to_basket(browser, link):
    item_page = ItemPage(browser, link)
    item_page.open()
    item_page.add_item_into_basket()
    item_page.solve_quiz_and_get_code()
    item_page.should_item_added()
