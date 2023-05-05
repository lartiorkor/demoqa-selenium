from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchWindowException
import pytest

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)


@pytest.fixture(scope='module')
def close_driver():
    # Setup
    yield
    # Teardown
    driver.quit()


def test_home_link(close_driver):
    driver.get("https://demoqa.com/links")
    home = driver.current_window_handle
    driver.find_element(By.LINK_TEXT, "Home").click()
    for window_handle in driver.window_handles:
        if window_handle != home:
            driver.switch_to.window(driver.window_handles[-1])
            assert "https://demoqa.com/" == driver.current_url
            break
    driver.close()


def test_dynamic_link(close_driver):
    try:
        driver.get("https://demoqa.com/links")
        home_tab = driver.current_window_handle
        driver.find_element(By.ID, "dynamicLink").click()
        for window_handle in driver.window_handles:
            if window_handle != home_tab:
                driver.switch_to.window(driver.window_handles[-1])
                assert "https://demoqa.com/" == driver.current_url
    except NoSuchWindowException:
        driver.quit()


def test_created_link(close_driver):
    try:
        driver.get("https://demoqa.com/links")
        driver.find_element(By.LINK_TEXT, "Created").click()
        p_tags = driver.find_elements(By.TAG_NAME, 'p')
        p_tags[-1].is_displayed()
    except:
        driver.quit()

# def test_no_content_link(close_driver):
#     driver.get("https://demoqa.com/links")
#     driver.find_element(By.LINK_TEXT, "No Content").click()
#     p_tags = driver.find_elements(By.TAG_NAME, 'p')
#     p_tags[-1].is_displayed()


# def test_moved_link(close_driver):
#     driver.get("https://demoqa.com/links")
#     driver.find_element(By.LINK_TEXT, "Moved").click()
#     p_tags = driver.find_elements(By.TAG_NAME, 'p')
#     p_tags[-1].is_displayed()


# def test_bad_request_link(close_driver):
#     driver.get("https://demoqa.com/links")
#     driver.find_element(By.LINK_TEXT, "Bad Request").click()
#     p_tags = driver.find_elements(By.TAG_NAME, 'p')
#     p_tags[-1].is_displayed()


# def test_unauthorized_link(close_driver):
#     driver.get("https://demoqa.com/links")
#     driver.find_element(By.LINK_TEXT, "Unauthorized").click()
#     p_tags = driver.find_elements(By.TAG_NAME, 'p')
#     p_tags[-1].is_displayed()


# def test_forbidden_link():
#     driver.get("https://demoqa.com/links")
#     try:
#         link = driver.find_element(By.LINK_TEXT, "Forbidden")
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(link)
#         )
#         driver.execute_script("arguments[0].scrollIntoView();", link)
#         link.click()
#         p_tags = driver.find_elements(By.TAG_NAME, 'p')
#         p_tags[-1].is_displayed()
#     finally:
#         driver.quit()


# def test_not_found_link():
#     driver.get("https://demoqa.com/links")
#     try:
#         link = driver.find_element(By.PARTIAL_LINK_TEXT, "Not Found")
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(link)
#         )
#         driver.execute_script("arguments[0].scrollIntoView();", link)
#         link.click()
#         p_tags = driver.find_elements(By.TAG_NAME, 'p')
#         p_tags[-1].is_displayed()
#     finally:
#         driver.quit()
