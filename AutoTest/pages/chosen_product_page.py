
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Select_product(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    price_filter = "//*[@id='p_36/11720402011']/span/a/span"
    os_select_filter = "//*[@id='p_n_feature_twenty-one_browse-bin/19711394011']/span/a/span"
    chose_product_1 = \
        "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span"
    chose_product_2 =\
        "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span"




    #Getters
    def get_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.price_filter)))

    def get_os_select_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.os_select_filter)))

    def get_chose_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.chose_product_1)))

    def get_chose_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.chose_product_2)))




    #actions
    def click_price_filter(self):
        self.get_price_filter().click()
        print("click price filter")

    def click_os_select_filter(self):
        self.get_os_select_filter().click()
        print("click os select filter")

    def click_chose_product_1(self):
        self.get_chose_product_1().click()
        print("click on select product")

    def click_chose_product_2(self):
        self.get_chose_product_2().click()
        print("click on select product")

    #Methods
    def add_to_cart_product_1(self, ):
        self.get_current_url()
        self.click_price_filter()
        self.click_os_select_filter()
        self.click_chose_product_1()

        print("good test")

    def add_to_cart_product_2(self):
        self.get_current_url()
        self.click_chose_product_2()

