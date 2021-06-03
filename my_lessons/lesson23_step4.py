from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    browser.find_element_by_css_selector("button.btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()