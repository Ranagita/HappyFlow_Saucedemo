from selenium import webdriver
from selenium.webdriver.common.by import By as by
from locators.login import LocatLogin, Std

class Valid:
    def __init__(self,driver):
        self.driver = driver
    
    def username(self):
        self.driver.find_element(by.ID,LocatLogin.input_username).send_keys(Std.user)
    
    def password(self):
        self.driver.find_element(by.ID,LocatLogin.input_password).send_keys(Std.password)

    def click_login_button(self):
        self.driver.find_element(by.XPATH,LocatLogin.login_button).click()


class Invalid:
    def __init__(self,driver):
        self.driver = driver

    def username(self,user):
        self.driver.find_element(by.ID,LocatLogin.input_username).send_keys(user)

    def password(self,pswd):
        self.driver.find_element(by.ID,LocatLogin.input_password).send_keys(pswd)
    
    def assertion(self):
        notif = self.driver.find_element(by.CSS_SELECTOR,"h3").text
        return notif
    