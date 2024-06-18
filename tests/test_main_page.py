import time
import allure
import pytest_check as check
from portfolio_s_borozna.locators.locators_main_page import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работоспособности хедера')
def test_main_page(web_browser):
    """Этот тест проверяет работоспособность хедера"""

    page = MainPage(web_browser)

    btn_headers = [(page.btn_headers_catalog, 'Каталог товаров', 'https://lakikraski.by/#'),
                   (page.btn_headers_brends, 'Бренды', 'https://lakikraski.by/brands/'),
                   (page.btn_headers_to_help, 'В помощь',
                    'https://lakikraski.by/#'),
                   (page.btn_headers_about_company, 'О компании', 'https://lakikraski.by/#'),
                   (page.btn_headers_contact, 'Контакты', 'https://lakikraski.by/kontakty-mir-cveta/'),
                   (page.btn_headers_basket, '', 'https://lakikraski.by/#'), (page.btn_headers_profile, '',
                                                                              'https://lakikraski.by/my-account/'),
                   (page.btn_headers_mc, '', 'https://lakikraski.by/')]

    for elements, text_elements, href_elements in btn_headers:
        with allure.step('Проверка на отображение'):
            check.is_true(elements.is_visible())

        with allure.step('Проверка на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста {elements}'):
            check.equal(elements.get_text(), text_elements)

        with allure.step(f'Сверка href {elements}'):
            check.equal(elements.get_attribute('href'), href_elements)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работоспособности поиска на главной странице')
def test_search_main_page(web_browser):
    """Этот тест проверяет работоспособность строки поиска на главной странице """

    page = MainPage(web_browser)

    with allure.step('Проверка на отображение'):
        check.is_true(page.headers_search.is_visible())

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.headers_search.is_clickable())

    with allure.step('Проверка плейсхолдера'):
        check.equal(page.headers_search.get_attribute('placeholder'), 'Поиск...')

    with allure.step('Проверка на ввод текста и его отображение'):
        input_test = ['Biora', '891']

        for i in input_test:
            page.headers_search.send_keys(i)
            time.sleep(5)
            check.not_equal(page.result_search.get_text().find(i), -1)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работоспособности обратной связи')
def test_feedback(web_browser):
    """Этот тест проверяет работоспособность кнопки обратная связь """

    page = MainPage(web_browser)

    with allure.step('Проверка на отображение кнопки Обратная связь'):
        check.is_true(page.btn_headers_feedback.is_visible())

    with allure.step('Проверка на кликабельность кнопки Обратная связь'):
        check.is_true(page.btn_headers_feedback.is_clickable())

    page.btn_headers_feedback.click()

    time.sleep(5)

    feedback = [page.inp_feedback_name, page.inp_feedback_phone, page.inp_feedback_email,
                page.inp_feedback_question, page.btn_feedback_send]

    for elements in feedback:
        with allure.step('Проверка на отображение полей для заполнения обратной связи'):
            check.is_true(elements.is_visible())

        with allure.step('Проверка на кликабельность полей для заполнения обратной связи'):
            check.is_true(elements.is_clickable())

    with allure.step('Проверка плейсхолдера'):
        check.equal(page.inp_feedback_name.get_attribute('placeholder'), 'Ваше Имя?')
        check.equal(page.inp_feedback_phone.get_attribute('placeholder'), '+375 29 123-45-67')
        check.equal(page.inp_feedback_email.get_attribute('placeholder'), 'Ваш Email адрес?')

    with allure.step('Проверка ввода текста и его отображение'):
        test_input = ['Пингвин', '+375 29 888 88 88', 'penguin@pen.by', 'Вы пингвины?']

        page.inp_feedback_name.send_keys(test_input[0])
        page.inp_feedback_phone.send_keys(test_input[1])
        page.inp_feedback_email.send_keys(test_input[2])
        page.inp_feedback_question.send_keys(test_input[3])

        check.equal(page.inp_feedback_name.get_text(), test_input[0])
        check.equal(page.inp_feedback_phone.get_text(), test_input[1])
        check.equal(page.inp_feedback_email.get_text(), test_input[2])
        check.equal(page.inp_feedback_question.get_text(), test_input[3])
