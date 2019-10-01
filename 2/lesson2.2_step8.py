from selenium import webdriver
import time
import os

try:
    # Открыть страницу http://suninjuly.github.io/file_input.html
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    get_el =  browser.find_element_by_css_selector
# Заполнить текстовые поля: имя, фамилия, email
    get_el('[name="firstname"]').send_keys('Ivan')
    get_el('[name="lastname"]').send_keys('Ivanov')
    get_el('[name="email"]').send_keys('ivanov@ivan.com')
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    get_el('#file').send_keys(file_path)
# Нажать кнопку "Submit"
    get_el('[type="submit"]').click()
finally:
    time.sleep(8)
    browser.quit
