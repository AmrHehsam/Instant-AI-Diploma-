import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#Path of chrome driver on your device
chromeDriver = "E:\AI Diploma\Instant AI Diploma\chromedriver-win64\chromedriver-win64\chromedriver.exe"


chromeOptions = Options()
chromeOptions.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(chromeDriver), options=chromeOptions)

driver.get("https://github.com")
time.sleep(3)

signinButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
signinButton.click()

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_field")))
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
username.send_keys("Enter your username Here")
password.send_keys("Enter your Password Here")
loginButton = driver.find_element(By.NAME, "commit")
loginButton.click()

time.sleep(10)

driver.quit()
