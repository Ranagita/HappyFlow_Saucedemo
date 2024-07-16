from selenium import webdriver
from selenium.webdriver.common.by import By as by

class Details:
    def __init__(self,driver):
        self.driver = driver
    
    def check_detail_name(self):
        detail = self.driver.find_element(by.XPATH,"//div[@class='inventory_details_name large_size']").text
        return detail
    
    def chx_price(self):
        price = self.driver.find_element(by.XPATH,"//div[@class='inventory_details_price']").text
        return price