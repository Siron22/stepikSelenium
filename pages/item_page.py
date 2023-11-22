from selenium.webdriver.common.by import By

from .base_page import BasePage


class ItemPageLocators:

    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_ADD_TO_THE_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1)")
    ALERT_SHIPPING = (By.CSS_SELECTOR, "div.alert:nth-child(2)")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert:nth-child(3)")
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, "a.btn-info:nth-child(1)")



class ItemPage(BasePage):
    def add_item_into_basket(self):
        add_button = self.browser.find_element(*ItemPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()

    def should_item_added(self):
        self.should_add_allert()
        self.should_shipping_allert()
        self.should_allert_basket_total()
        self.should_button_view_basket()

    def should_add_allert(self):
        assert self.is_element_present(*ItemPageLocators.ALERT_ADD_TO_THE_BASKET), \
            "Alert add to the basket is not presented"

    def should_shipping_allert(self):
        assert self.is_element_present(*ItemPageLocators.ALERT_SHIPPING), \
            "Alert shipping to the basket is not presented"

    def should_allert_basket_total(self):
        assert self.is_element_present(*ItemPageLocators.ALERT_BASKET_TOTAL), \
            "Basket total alert  is not presented"

    def should_button_view_basket(self):
        assert self.is_element_present(*ItemPageLocators.BUTTON_VIEW_BASKET), \
            "Button view basket is not presented"






