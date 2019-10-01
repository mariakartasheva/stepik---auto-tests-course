from selenium import webdriver
import math
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)
    input_checkbox = browser.find_element_by_id("robotCheckbox")
    input_checkbox.click()
    input_radiobutton = browser.find_element_by_id("robotsRule")
    input_radiobutton.click()
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла