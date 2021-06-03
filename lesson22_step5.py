# from selenium import webdriver
#
# browser = webdriver.Chrome()
# # browser.execute_script("alert('Robots at work');")
# browser.execute_script("document.title='Script executed'; alert('Robots at work')")

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # browser.execute_script("window.scrollBy(0, 100);")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()