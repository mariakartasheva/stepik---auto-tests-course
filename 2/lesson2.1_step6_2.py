import selenium.webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link ='http://suninjuly.github.io/get_attribute.html'
    browser = selenium.webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input_answer = browser.find_element_by_css_selector('#answer')
    input_answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()
    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()
finally:
    time.sleep(8)
    browser.quit()
