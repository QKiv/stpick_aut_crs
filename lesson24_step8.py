from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # дожидаемся когда цена дома упадет до 100%
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    # находим число и отправляем получившиеся значение
    browser.find_element_by_id("book").click()
    number = browser.find_element_by_id("input_value").text
    y = calc(number)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("solve").click()
    browser.switch_to.alert

finally:
    time.sleep(10)
    browser.quit()