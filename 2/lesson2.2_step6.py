from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу http://SunInJuly.github.io/execute_script.html.
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
# Считать значение для переменной x.
    x = browser.find_element_by_id('input_value').text
# Посчитать математическую функцию от x.
    y = calc(x)
# Ввести ответ в текстовое поле.
    browser.find_element_by_css_selector('#answer').send_keys(y)
# Выбрать checkbox "I'm the robot".
    browser.find_element_by_css_selector('#robotCheckbox').click()
# Переключить radiobutton "Robots rule!".
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
# Проскроллить страницу вниз.
    submit_button = browser.find_element_by_css_selector('[type="submit"]')
# Нажать на кнопку "Submit".
    submit_button.click()

finally:
    time.sleep(8)
    browser.quit
# пустая строка
