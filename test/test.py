from selenium import webdriver
from selenium.webdriver.common.by import By as by
from pages.login import Valid, Invalid, Valid
from pages.inventory import Inventory
from pages.details import Details
from pages.cart import Cart
import pytest

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

@pytest.mark.positive
def test_login(setup):
    valid = Valid(setup)
    inventory = Inventory(setup)

    valid.username()
    valid.password()
    valid.click_login_button()

    title = inventory.check_title()
    assert title=="Swag Labs"


def test_add_to_cart(setup):
    valid = Valid(setup)
    inventory = Inventory(setup)
    detail = Details(setup)
    cart = Cart(setup)

    # Login with valid credential
    valid.username()
    valid.password()
    valid.click_login_button()

    # Select item
    inventory.select_item()

    item = detail.check_detail_name()
    price = detail.chx_price()

    assert item=="Sauce Labs Backpack"
    assert price=="$29.99"

    # Add to cart and assertion
    cart.add_to_cart()
    cart.cart_button()
    assertion = cart.cart_assert()
    assert assertion=="Your Cart"

invalid = [
        ("standard_user","sentot"),
        ("sentot","secret_sauce"),
        ("sentot","sentot")
    ]

@pytest.mark.parametrize("user,pswd",invalid)
def test_invalid_login(setup, user, pswd):
    valid = Valid(setup)
    invalid = Invalid(setup)
    
    invalid.username(user)
    invalid.password(pswd)
    valid.click_login_button()

    # assertion
    notif = invalid.assertion()
    assert notif=="Epic sadface: Username and password do not match any user in this service"