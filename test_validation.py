from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.minimize_window()
driver.implicitly_wait(1)

def test_login():
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    driver.implicitly_wait(2)
    Title = driver.find_element(By.CLASS_NAME,"title").text
    assert Title=="Products"

Kunci = [
    ("//div[.='Sauce Labs Backpack']","Sauce Labs Backpack","$29.99"),
    ("//div[.='Sauce Labs Bike Light']","Sauce Labs Bike Light","$9.99"),
    ("//div[.='Sauce Labs Bolt T-Shirt']","Sauce Labs Bolt T-Shirt","$15.99"),
    ("//div[.='Sauce Labs Fleece Jacket']","Sauce Labs Fleece Jacket","$49.99"),
    ("//div[.='Sauce Labs Onesie']","Sauce Labs Onesie","$7.99"),
    ("//div[.='Test.allTheThings() T-Shirt (Red)']","Test.allTheThings() T-Shirt (Red)","$15.99")
    ]

@pytest.mark.parametrize("a,b,c",Kunci)
def test_interaction(a,b,c):
    driver.find_element(By.XPATH,a).click()
    Wait = driver.implicitly_wait(2)
    Title = driver.find_element(By.CSS_SELECTOR,".inventory_details_name").text
    assert Title==b
    Price = driver.find_element(By.CSS_SELECTOR,".inventory_details_price").text
    assert Price==c
    driver.find_element(By.ID,"add-to-cart").click()
    Wait
    driver.find_element(By.ID,"back-to-products").click()
    Wait
    Title2 = driver.find_element(By.CLASS_NAME,"title").text
    assert Title2=="Products"
