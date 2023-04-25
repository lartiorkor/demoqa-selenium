from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pytest

options = Options()
options.add_experimental_option('detach', True)
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

# move this guy out to somewhere else


@pytest.fixture(scope='module')
def close_driver():
    # Setup
    yield
    # Teardown
    driver.quit()


@pytest.fixture
def visit_buttons_url():
    driver.get("https://demoqa.com/buttons")


def test_navigation(close_driver):
    driver.get("https://demoqa.com/")
    element_card = driver.find_element(By.CLASS_NAME, "card-up")
    element_card.click()
    assert "https://demoqa.com/elements" == driver.current_url, "Url does not match driver.current_url"
    button_element = driver.find_element(By.ID, "item-4")
    button_element.click()
    assert "https://demoqa.com/buttons" == driver.current_url, "Url does not match driver.current_url"


def test_double_click_button(close_driver):
    driver.get("https://demoqa.com/buttons")
    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(double_click_btn).perform()
    assert driver.find_element(By.ID, "doubleClickMessage").is_displayed()


def test_right_click_button(close_driver):
    driver.get("https://demoqa.com/buttons")
    right_click_btn = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(right_click_btn).perform()
    assert driver.find_element(By.ID, "rightClickMessage").is_displayed()


def test_left_click_button(close_driver):
    driver.get("https://demoqa.com/buttons")
    btns = driver.find_elements(By.TAG_NAME, "button")
    btns[3].click()
    assert driver.find_element(By.ID, "dynamicClickMessage").is_displayed()
