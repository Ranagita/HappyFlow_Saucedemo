from selenium import webdriver
from selenium.webdriver.common.by import By as by
from locators.inventory import Inventory_1 as inv_1

class Inventory:
    def __init__(self,driver):
        self.driver = driver

    def check_title(self):
        title = self.driver.find_element(by.XPATH,"//div[@class='app_logo']").text
        return title
    
    def select_item(self):
        self.driver.find_element(by.XPATH,inv_1.item).click()
    
    def check_item(self):
        item = self.driver.find_element(by.XPATH,"//div[@class='inventory_details_name large_size']").text
        return item
    
    def check_price(self):
        price = self.driver.find_element(by.XPATH,"//div[@class='inventory_details_price']").text
        return price
    
