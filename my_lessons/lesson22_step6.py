from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # находим и вычисляет по формуле Х
    x_number = browser.find_element_by_id("input_value").text
    y = calc(x_number)

    # скролим и вписываем число Y
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("answer").send_keys(y)

    # нажимаем на радио баттоны

    option1 = browser.find_element_by_id("robotCheckbox").click()
    option2 = browser.find_element_by_id("robotsRule").click()

    # нажимаем на субмит

    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()