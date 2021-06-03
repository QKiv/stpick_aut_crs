from selenium import webdriver
import os, time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("test")
    browser.find_element_by_name("lastname").send_keys("test")
    browser.find_element_by_name("email").send_keys("test@test.test")

    # создаем файл

    with open('file.txt', 'w') as ouf:
        ouf.write("Hello")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла
    browser.find_element_by_id("file").send_keys(file_path)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()