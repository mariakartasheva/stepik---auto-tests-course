from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    browser.get(link)
# Нажать на кнопку
    get_el = browser.find_element_by_css_selector
    get_el('[type="submit"]').click()
    # time.sleep(1)
# Переключиться на новую вкладку
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
# Пройти капчу для робота и получить число-ответ
    x = get_el('#input_value').text
    y = calc(x)
    get_el('#answer').send_keys(y)
    get_el('[type="submit"]').click()
finally:
    time.sleep(8)
    browser.quit
