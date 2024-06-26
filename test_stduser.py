from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
wait = driver.implicitly_wait(1)

def test_login():    
    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH,"//input[@id='login-button']").click()
    wait
    Title = driver.find_element(By.CLASS_NAME,"title").text
    
    assert Title=="Products"

ToCart = [
    ("//button[@id='add-to-cart-sauce-labs-backpack']"),
    ("//button[@id='add-to-cart-sauce-labs-bike-light']"),
    ("//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"),
    ("//button[@id='add-to-cart-sauce-labs-fleece-jacket']"),
    ("//button[@id='add-to-cart-sauce-labs-onesie']"),
    ("//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    ]

@pytest.mark.parametrize('a',ToCart)
def test_add_items(a):
    driver.find_element(By.XPATH,a).click()

wait

def test_shopping_cart():
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    Title = driver.find_element(By.CLASS_NAME,"title").text
    assert Title=="Your Cart"

wait

Remove =[
    ("remove-sauce-labs-backpack"),
    ("remove-sauce-labs-bike-light"),
    ("remove-sauce-labs-bolt-t-shirt"),
    ("remove-sauce-labs-fleece-jacket"),
    ("remove-sauce-labs-onesie"),
    ("remove-test.allthethings()-t-shirt-(red)")
    ]

@pytest.mark.parametrize('a',Remove)
def test_remove_item_from_cart(a):
    driver.find_element(By.ID,a).click()

wait

def test_return_to_homepage_from_cart():
    driver.find_element(By.ID,"continue-shopping").click()
    wait
    Title = driver.find_element(By.CLASS_NAME, "title").text
    assert Title=="Products"

wait

ToCart2 = [
    ("//button[@id='add-to-cart-sauce-labs-backpack']"),
    ("//button[@id='add-to-cart-sauce-labs-bike-light']"),
    ("//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"),
    ("//button[@id='add-to-cart-sauce-labs-fleece-jacket']"),
    ("//button[@id='add-to-cart-sauce-labs-onesie']"),
    ("//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    ]

@pytest.mark.parametrize('a',ToCart2)
def test_re_add_items(a):
    driver.find_element(By.XPATH,a).click()

wait

def test_to_shopping_cart():
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    Title = driver.find_element(By.CLASS_NAME,"title").text
    assert Title=="Your Cart"

def test_check_out():
    driver.find_element(By.ID,"checkout").click()
    Title = driver.find_element(By.CLASS_NAME,"title").text
    assert Title=="Checkout: Your Information"
    driver.find_element(By.ID,"first-name").send_keys("Pawang")
    driver.find_element(By.ID,"last-name").send_keys("Python")
    driver.find_element(By.ID,"postal-code").send_keys("777")
    driver.find_element(By.ID,"continue").click()
    Title2 = driver.find_element(By.CLASS_NAME,"title").text
    assert Title2=="Checkout: Overview"

def test_finish():
    Item = driver.find_element(By.CLASS_NAME,"summary_subtotal_label").text
    Tax = driver.find_element(By.CLASS_NAME,"summary_tax_label").text
    Total = driver.find_element(By.CLASS_NAME,"summary_total_label").text
    # assert (Item+Tax)==Total
    wait
    driver.find_element(By.ID,"finish").click()
    driver.find_element(By.ID,"back-to-products").click()
    wait
    driver.find_element(By.ID,"react-burger-menu-btn").click()
    driver.find_element(By.ID,"logout_sidebar_link").click()

# def test_quit():
#     driver.close
#     driver.quit

    
