
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    url = 'https://www.amazon.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    menu_button = "//*[@id='nav-hamburger-menu']/i"
    menu_see_all_button = "//*[@id='hmenu-content']/ul[1]/li[11]/a[1]"
    menu_software_button = "//*[@id='hmenu-content']/ul[1]/ul[1]/li[15]/a"
    menu_operation_systems_button = "//*[@id='hmenu-content']/ul[50]/li[14]/a"
    search_place = "//*[@id='twotabsearchtextbox']"


    #Getters
    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.menu_button)))

    def get_menu_see_all_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.menu_see_all_button)))

    def get_menu_software_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable ((By.XPATH,self.menu_software_button)))

    def get_menu_operation_systems_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.menu_operation_systems_button)))

    def get_search_place(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_place)))


    #actions
    def click_menu_button(self):
        self.get_menu_button().click()
        print("click menu button")

    def click_menu_see_all_button(self):
        self.get_menu_see_all_button().click()
        print("click menu see all button")

    def click_menu_software_button(self):
        self.get_menu_software_button().click()
        print("click menu software button")

    def click_menu_operation_systems_button(self):
        self.get_menu_operation_systems_button().click()
        print("click menu_button")

    #
    def input_search_place(self, product_name_2):
        self.get_search_place().send_keys(product_name_2)
        self.get_search_place().send_keys(Keys.RETURN)
        print("input product name (2)")



    #Methods
    def select_product_os(self,):
        self.driver.get(self.url)
        self.get_current_url()
        self.driver.maximize_window()
        self.click_menu_button()
        self.click_menu_see_all_button()
        self.click_menu_software_button()
        self.click_menu_operation_systems_button()
        print("good test")

    def search_product_game(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.driver.maximize_window()
        self.input_search_place("DOOM Game")

