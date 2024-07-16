import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By as by

@pytest.fixture
def setup():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(7)
    yield driver
    driver.quit()


credentials = {
    ("sentot","secret_sauce"),
    ("standard_user","sentot"),
    ("sentot","sentot")
}

@pytest.mark.parametrize('a,b',credentials)
def test_add_to_cart(setup,a,b):
    setup.find_element(by.ID,"user-name").send_keys(a)
    setup.find_element(by.ID,"password").send_keys(b)
    setup.find_element(by.ID,"login-button").click()

    notif = setup.find_element(by.CSS_SELECTOR,"h3").text
    assert notif=="Epic sadface: Username and password do not match any user in this service"
