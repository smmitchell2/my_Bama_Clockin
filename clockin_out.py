import sys
import time
import json
import timeit
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait

def main():
    time.sleep(10800)
    browser = webdriver.Firefox(executable_path=r'/Users/aimestudent2/Downloads/geckodriver')
    browser.get('https://login.ua.edu/cas/login?service=https%3A%2F%2Fmybama.ua.edu%2Fc%2Fportal%2Flogin')
    loginElem = browser.find_element_by_id('username')
    loginElem.send_keys(‘username goes here’)
    passwordElem = browser.find_element_by_id('password')
    passwordElem.send_keys('password goes here')
    passwordElem.submit()
    time.sleep(5)

    browser.find_element_by_link_text("Employee").click()
    browser.get("https://bnrsupport.ua.edu/CASSSO/action/wfsso")
    time.sleep(2)
    browser.find_element_by_link_text("Clock Out").click()
    

    browser.close()
    
    return 0

main()


