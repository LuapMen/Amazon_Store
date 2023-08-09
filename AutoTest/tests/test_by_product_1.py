import time
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Proced_to_checkout
from pages.chosen_product_page import Select_product
from pages.main_page import Main_page
from pages.product_page import Add_to_cart


def test_buy_product_1():
    os.environ['PATH'] += ';E:\\Project\\Project_Amazon\\Driver'
    driver = webdriver.Chrome()

    print("Start Test")

    main_page = Main_page(driver)
    main_page.select_product_os()

    chose_product = Select_product(driver)
    chose_product.add_to_cart_product_1()

    product_1 = Add_to_cart(driver)
    product_1.go_to_cart_page_1()

    cart_page = Proced_to_checkout(driver)
    cart_page.go_to_checkout()


    time.sleep(5)

