from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    link = ""
    browser.get(link)

    alert1 = browser.switch_to.alert
    alert1.accept()

    alert2 = browser.switch_to.alert
    alert2_text = alert2.text

    confirm = browser.switch_to.alert
    confirm.accept()
    confirm.dismiss()

    prompt = browser.switch_to.alert
    prompt.send_keys("Answer")
    prompt.accept()