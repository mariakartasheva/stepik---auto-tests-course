from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
get_el = browser.find_element_by_css_selector

try:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
# Нажать на кнопку "Book"
    get_el('#book').click()
# Пройти капчу для робота и получить число-ответ
    x = get_el('#input_value').text
    y = calc(x)
    get_el('#answer').send_keys(y)
    get_el('[type="submit"]').click()
finally:
    time.sleep(8)
    browser.quit
