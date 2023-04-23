from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)


driver.get("https://demoqa.com/upload-download")
# driver.find_element(By.ID, "downloadButton").click()

# .send_keys("sampleFile (2)")
input = driver.find_element(By.ID, "uploadFile")
input.click()
# driver.find_element(By.ID,"uploadFile").submit()
# if(driver.page_source.find("Choose File")):
#     print("file upload success")
# else:
#     print("file upload not successful")
print("file upload not successful")
driver.quit()
