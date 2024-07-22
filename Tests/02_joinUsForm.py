from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

fullname = "Swarup Kumar Rath"
email = "justsonu2.0@gmail.com"

PATH = "C:/Users/SONU/Desktop/selenium-webTesting-master/selenium-webTesting-master/Browsers/chromedriver.exe"

service = Service(executable_path=PATH)

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.thesparksfoundationsingapore.org/join-us/why-join-us/#")

try:

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]").send_keys(fullname)
    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]").send_keys(email)
    time.sleep(3)

    dropdown = Select(driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/select"))
    dropdown.select_by_index(1) 
    time.sleep(3)


    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/form/input[@type='submit']").send_keys(Keys.RETURN)
    time.sleep(3)

    print("The test is completed successfully by submitting form data")

finally:

    driver.quit()
