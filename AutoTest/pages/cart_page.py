import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Proced_to_checkout(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    all_price_cart = "//*[@id='sc-subtotal-amount-activecart']/span"
    checkout_button = "//*[@id='sc-buy-box-ptc-button']/span/input"




    #Getters

    def get_all_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.all_price_cart)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.checkout_button)))


    #actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("click checkout button")


    #Methods
    def go_to_checkout(self):
        self.get_current_url()
        self.output_name_product(self.get_all_price_cart())
        time.sleep(10)
        self.get_screenshot("test_by_product")
        self.click_checkout_button()

        print("good test")
