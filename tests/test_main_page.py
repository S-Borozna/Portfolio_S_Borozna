import time

import pytest_check as check
from Portfolio_S_Borozna.locators.locators_main_page import MainPage


def test_search(web_browser):
    """Этот тест проверяет поиск"""

    page = MainPage(web_browser)

    elements_search = [ page.hed_search, page.btn_search]


    for el in elements_search:
         check.is_true(el.is_visible())
         check.is_true(el.is_clickable())

    check.equal(page.hed_search.get_attribute('placeholder'),"Введите домены")

    text_inp ='m/+\*)(^%!#$^&'
    page.hed_search.send_keys(text_inp)
    page.btn_search.click()
    check.equal(page.txt1.get_text(), 'Имя домена должно содержать от 2 до 63 символов')
    check.equal(page.txt2.get_text(), 'Символы "/", "+", "\", "*", ")", "(", "^", "%", "!", "#", "$", "&" удалены, '
                           'т.к. являются недопустимыми.')
    page.go_back()


    inp = ['tryam','vivat','my']
    for i in inp:
        dom = i + page.var_dom.get_text()

        page.hed_search.send_keys(i)
        page.btn_search.click()
        time.sleep(5)
        check.not_equal(page.rez.get_text().find(dom),-1)
        page.go_back()