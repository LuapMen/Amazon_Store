
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Add_to_cart(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    product_name_1 = "//*[@id='productTitle']"
    product_name_2 = "//*[@id='title']"
    add_to_cart = "//*[@id='add-to-cart-button']"
    go_to_cart = "//*[@id='sw-gtc']/span/a"




    #Getters
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.product_name_1)))

    def get_product_name_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.product_name_2)))

    def get_add_1_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.add_to_cart)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.go_to_cart)))


    #actions

    def click_add_1_to_cart(self):
        self.get_add_1_to_cart().click()
        print("Click to add cart")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("click go to cart")


    #Methods
    def go_to_cart_page_1(self, ):
        self.get_current_url()
        self.output_name_product(self.get_product_name_1())
        self.click_add_1_to_cart()
        self.click_go_to_cart()
        print("good test")

    def go_to_cart_page_2(self, ):
        self.get_current_url()
        self.output_name_product(self.get_product_name_2())
        self.click_add_1_to_cart()
        self.click_go_to_cart()
        print("good test")

