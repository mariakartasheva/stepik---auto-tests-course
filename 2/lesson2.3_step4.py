from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
# Нажать на кнопку
    get_el = browser.find_element_by_css_selector
    get_el('[type="submit"]').click()
# Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
# На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = get_el('#input_value').text
    y = calc(x)
    get_el('#answer').send_keys(y)
    get_el('[type="submit"]').click()
finally:
    time.sleep(8)
    browser.quit
