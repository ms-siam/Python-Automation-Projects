#! python3
# cliEmailer.py- takes an email address and string of text , 
# then login to email account and sends the email to the provided address

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/v3/signin/identifier?hl=en-gb&ifkv=ASSHykqVNSa7tl4sL8AOTvtuRy7Qxgf8--TGGsE1B8RoiNJDqwg6frneSJQRxfKkgOgot1ayFiqf&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S541183%3A1739431178159529&ddm=1')
userEmail = browser.find_element('id', 'identifierId')
