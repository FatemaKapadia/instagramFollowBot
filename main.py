from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from instaFollower import InstaFollower


keywords = ["chef", "food"]

bot = InstaFollower()
bot.login()

for x in keywords:
    bot.find_followers(x)
    bot.follow()

bot.end()


