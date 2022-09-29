from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--no-sandbox")


# START DRIVER

driver = webdriver.Chrome(service=Service('/home/dima/Завантаження/Hillel/chromedriver'), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

#GET ATTRIBUTE
# signIn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).get_attribute("value")

#CLICK by clickable
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

#CLICK be presense
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

elements = driver.find_elements(By.XPATH, '//button')
print(len(elements))
assert len(elements) > 0
# elem = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
# elem.click()



# goButton = driver.find_element(By.ID, "submit")
# goButton.click()

assert "No results found." not in driver.page_source
driver.close()
