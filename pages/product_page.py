from selenium.webdriver.common.by import By

from .base_page import BasePage


class ProductPageLocators:

    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_ADD_TO_THE_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1)")
    ALERT_SHIPPING = (By.CSS_SELECTOR, "div.alert:nth-child(2)")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert:nth-child(3)")
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, "a.btn-info:nth-child(1)")
    ITEM_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    ALERT_NAME = (By.XPATH, "//div[1]/div[1]/strong")


class ProductPage(BasePage):

    def add_item_into_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()

    def should_item_added(self):
        self.should_add_alert()
        self.should_shipping_alert()
        self.should_alert_basket_total()
        self.should_button_view_basket()
        self.should_item_name_add()

    def should_add_alert(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADD_TO_THE_BASKET), \
            "Alert add to the basket is not presented"

    def should_not_add_alert(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADD_TO_THE_BASKET), \
            "Alert add to the basket is presented, but should not"

    def should_add_alert_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ADD_TO_THE_BASKET), \
            "Alert add to the basket is disappear"

    def should_shipping_alert(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SHIPPING), \
            "Alert shipping to the basket is not presented"

    def should_alert_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_BASKET_TOTAL), \
            "Basket total alert  is not presented"

    def should_button_view_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_VIEW_BASKET), \
            "Button view basket is not presented"


    def should_item_name_add(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME).text
        assert item_name == alert_name, \
            "Name in the basket is not correct"

