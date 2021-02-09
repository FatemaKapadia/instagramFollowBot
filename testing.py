import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_web_driver = "D:\Program Files\Chromedriver\chromedriver.exe"
URL = "https://www.instagram.com/basketball/"
login_email = "botfatema@gmail.com"
password = "bothoonmai"
keywords = ["basketball"]

driver = webdriver.Chrome(executable_path=chrome_web_driver)

driver.get(URL)
time.sleep(5)
followers = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followers.click()

followers.send_keys(Keys.END)