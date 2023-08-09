import time
from selenium import webdriver
import os


from pages.cart_page import Proced_to_checkout
from pages.chosen_product_page import Select_product
from pages.main_page import Main_page
from pages.product_page import Add_to_cart


def test_buy_product_1():
    os.environ['PATH'] += ';E:\\Project\\Project_Amazon\\Driver'
    driver = webdriver.Chrome()

    print("Start Test")

    main_page = Main_page(driver)
    main_page.search_product_game()

    chose_product = Select_product(driver)
    chose_product.add_to_cart_product_2()
    #
    product_1 = Add_to_cart(driver)
    product_1.go_to_cart_page_2()
    #
    cart_page = Proced_to_checkout(driver)
    cart_page.go_to_checkout()


    time.sleep(5)

