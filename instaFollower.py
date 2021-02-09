from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_web_driver = "D:\Program Files\Chromedriver\chromedriver.exe"
URL = "https://www.instagram.com/"
login_email = "botfatema@gmail.com"
password = "bothoonmai"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_web_driver)

    def login(self):
        self.driver.get(URL)
        time.sleep(5)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(login_email)

        pw = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)

        time.sleep(10)

    def find_followers(self, x):
        search_box = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_box.send_keys(x)
        time.sleep(5)
        top_element = self.driver.find_element_by_class_name("yCE8d")

        try:
            top_element.click()
            time.sleep(5)

        except ElementClickInterceptedException:
            notifications = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            notifications.click()
            top_element.click()
            time.sleep(5)

    def follow(self):
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(5)
        followers_list = self.driver.find_element_by_class_name("isgrP")
        for j in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments['
                                       '0].offsetHeight;', followers_list)

        buttons = self.driver.find_elements_by_css_selector("li button")

        for x in buttons:
            try:
                x.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                time.sleep(1)
                cancel = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel.click()

        close = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button')
        close.click()

    def end(self):
        self.driver.quit()
