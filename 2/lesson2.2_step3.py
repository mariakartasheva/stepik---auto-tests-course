from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    y = browser.find_element_by_css_selector('#num1').text
    z = browser.find_element_by_css_selector('#num2').text
    x = str(int(y)+int(z))

    list_of_items = Select(browser.find_element_by_tag_name('select'))
    list_of_items.select_by_value(x)

    browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(8)
    browser.quit()

# Пустая строка
