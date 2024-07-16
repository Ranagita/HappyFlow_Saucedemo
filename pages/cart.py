from selenium import webdriver
from selenium.webdriver.common.by import By as by

class Cart:
    def __init__(self,driver):
        self.driver = driver
    
    def add_to_cart(self):
        self.driver.find_element(by.ID,"add-to-cart").click()

    def cart_button(self):
        self.driver.find_element(by.XPATH,"//a[@class='shopping_cart_link']").click()
    
    def cart_assert(self):
        cart_title = self.driver.find_element(by.XPATH,"//span[@class='title']").text
        return cart_title