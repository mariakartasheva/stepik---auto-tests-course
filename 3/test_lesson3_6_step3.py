from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import math
import time


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_feedback_is_correct(browser, lesson):
    get_el = browser.find_element
    # открыть страницу
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
# ввести правильный ответ
    answer = math.log(int(time.time()))
    textarea = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.textarea')))
    textarea.send_keys(str(answer))
# нажать кнопку "Отправить"
    get_el(By.CSS_SELECTOR, '.submit-submission').click()
# дождаться фидбека о том, что ответ правильный
    feedback = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    # time.sleep(5)
    assert feedback.text == "Correct!", 'Feedback should be "Correct!"'
# закрыть браузер.
    browser.quit()
