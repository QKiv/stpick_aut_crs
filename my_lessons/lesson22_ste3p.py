from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id("num1").text
    number2 = browser.find_element_by_id("num2").text
    print(number1, number2, number1 + number2)
    new_number = int(number1) + int(number2)

    spisok = Select(browser.find_element_by_tag_name("select"))
    spisok.select_by_value(str(new_number))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()