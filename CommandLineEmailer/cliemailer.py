#! python3
# cliEmailer.py- takes an email address and string of text , 
# then login to email account and sends the email to the provided address

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/')
userEmail = browser.find_element('id', 'identifierId')
userEmail.send_keys('mobaroksiam46')
nextElem = browser.find_element('id', 'identifierNext')
nextElem.click()
wait = WebDriverWait(browser, 10)

