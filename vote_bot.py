from selenium import webdriver
import random
import urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
import time
import requests

delayTime = 2
PATH = "C:\webdrivers\chromedriver.exe"


class VoteBot():

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
        time.sleep(random.randint(2, 3))

    def vote(self):
        self.driver.get(
            'https://bliskociebie.inpost.pl/blisko-ciebie/glosuj-na-miejsce#50.768410,20.635270')
        self.driver.find_element_by_id("onetrust-accept-btn-handler")
        self.driver.find_element_by_class_name(
            'banner-actions-container').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('voteButtonValidate').click()
        time.sleep(1)
        # self.driver.find_element_by_id("checkbox_id").click()
        # self.driver.find_element_by_class_name('goog-inline-block').click()
        g_recaptcha = self.driver.find_elements_by_class_name('g-recaptcha')[0]

        outerIframe = g_recaptcha.find_element_by_tag_name('iframe')
        outerIframe.click()

        iframes = self.driver.find_elements_by_tag_name('iframe')

        for index in range(len(iframes)):
            self.driver.switch_to.default_content()
            iframe = self.driver.find_elements_by_tag_name('iframe')[index]
            self.driver.switch_to.frame(iframe)
            self.driver.implicitly_wait(delayTime)
        time.sleep(5)
        self.driver.find_element_by_class_name('voteButtonTrigger').click()
        self.driver.close()


while True:
    bot = VoteBot()
    bot.vote()
