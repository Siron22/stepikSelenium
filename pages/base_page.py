from selenium.common import ElementNotInteractableException, TimeoutException, InvalidElementStateException, \
    StaleElementReferenceException

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (ElementNotInteractableException, TimeoutException, InvalidElementStateException,
                StaleElementReferenceException):
            return False
        return True
