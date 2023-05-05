# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from pathlib import Path

# BASE_DIR = Path(__file__).parent
# sample_file_path = BASE_DIR / 'sampleFile.jpeg'

# options = Options()
# options.add_experimental_option('detach', True)

# driver = webdriver.Chrome(options=options)
# actions = ActionChains(driver)


# def test_file_download():
#     driver.get("https://demoqa.com/upload-download")
#     driver.find_element(By.ID, "downloadButton").click()
#     with open(sample_file_path, 'r') as file:
#         file.read()


# def test_upload_button():
#     driver.get("https://demoqa.com/upload-download")
#     try:
#         upload_btn = driver.find_element(By.ID, "uploadFile")
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(upload_btn)
#         )
#         driver.execute_script("arguments[0].scrollIntoView();", upload_btn)
#         upload_btn.send_keys(str(sample_file_path))
#         print('goat')
#     finally:
#         driver.quit()
