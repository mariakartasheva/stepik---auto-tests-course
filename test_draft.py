import time


def test_add_to_basket_exists(browser):
    # Открыть страницу
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."
    browser.get(link)
# Найти кнопку добавления в корзину на странице.
    try:
        browser.find_element_by_css_selector('.btn-add-to-baske')
    except:
        assert False, '"Add to basket" does not exist on the page.'
    time.sleep(5)
