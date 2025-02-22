#! python3
# cliEmailer.py- takes an email address and string of text , 
# then login to email account and sends the email to the provided address

from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyinputplus as pyip
from selenium.webdriver.common.keys import Keys
import time
'''
# Google is blocking programmetically login 

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/')
userEmail = browser.find_element('id', 'identifierId')
userEmail.send_keys('mobaroksiam46')
nextElem = browser.find_element('id', 'identifierNext')
nextElem.click()
time.sleep(2)
wait = WebDriverWait(browser, 10)
userPass = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))

userPass.send_keys(pyip.inputPassword('Type your gmail password here. '))
passNextElem = browser.find_element('id', 'passwordNext')
passNextElem.click()
'''
#Using chrome browser , which is already logged in with a gmail

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  # Helps bypass bot detection

browser = webdriver.Chrome(options=options)

# Apply stealth settings
stealth(browser,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

browser.get('https://mail.google.com/mail/u/0/')

wait = WebDriverWait(browser, 10)  # Define wait

composeButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Compose']")))
composeButton.click()

reciepentElem = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=':ty']")))
reciepentElem.send_keys(pyip.inputEmail("Type reciepent's email address. "))
reciepentElem.send_keys(Keys.ENTER)

subjectElem = wait.until(EC.presence_of_element_located((By.NAME, "subjectbox")))
subjectElem.click()
subjectElem.send_keys(pyip.inputStr("Type your email subject here. ")) 

messageBody = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @aria-label='Message Body']")))
messageBody.click()
messageBody.send_keys(pyip.inputStr("Type your message for email. "))
messageBody.send_keys(Keys.CONTROL, Keys.RETURN)

