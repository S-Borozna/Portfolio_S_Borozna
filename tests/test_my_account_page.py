import time
import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from locators.locators_my_account_page import MyAccountPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работспособности кнопки мой аккаунт')
def test_my_account(web_browser):
    """Этот тест проверяет работоспособность кнопки мой аккаунт"""

    page = MainPage(web_browser)

    with allure.step('Проверка на отображение'):
        check.is_true(page.btn_headers_profile.is_visible())

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.btn_headers_profile.is_clickable())

    with allure.step(f'Сверка title'):
        check.equal(page.btn_headers_profile.get_attribute('title'), 'Мой аккаунт')

    with allure.step(f'Сверка href '):
        check.equal(page.btn_headers_profile.get_attribute('href'), 'https://lakikraski.by/my-account/')

@allure.story('Тест для проверки страницы "Мой аккаунт"')
@allure.feature('Тест для проверки работоспособности регистрации аккаунта')
def test_registration(web_browser):
    """Этот тест проверяет возможность зарегистрировать новый аккаунт"""

    page = MyAccountPage(web_browser)

    inp_email_neval = ['','tryam/tryam@tryam']
    inp_email_val = ['ya.svetochka17@gmail.com']

    with allure.step('Проверка на отображение'):
        check.is_true(page.inp_email_registration.is_visible())
        check.is_true(page.btn_registration.is_visible())

    with allure.step('Проверка на кликабельность'):
        check.is_true((page.btn_registration.is_clickable()))

    with allure.step('Проверка ввода и отображения текста'):
        page.inp_email_registration.send_keys(inp_email_val[0])
       # check.equal(page.inp_email_registration.get_text(),inp_email_val[0])

    with allure.step('Проверка регистрации с невалидными значениями'):
        for inp in inp_email_neval:
            page.inp_email_registration.send_keys(inp)
            page.btn_registration.click()
            check.equal(page.msg_error.get_text(),'Ошибка: Пожалуйста, укажите действующий адрес электронной почты.')

    with allure.step('Проверка регистрации с валидными значениями'):
        page.inp_email_registration.send_keys(inp_email_val[0])
        page.btn_registration.click()
        check.not_equal(page.msg_successful_registration.get_text().find('Из главной страницы аккаунта вы можете '
                                                                         'посмотреть ваши недавние заказы'), -1)

@allure.story('Тест для проверки страницы "Мой аккаунт"')
@allure.feature('Тест для проверки работоспособности формы входа в аккаунт')
def test_login_to_account(web_browser):
    """Этот тест проверяет возможность зайти в существуюющий аккаунт"""

    page = MyAccountPage(web_browser)

    login = 'ms.borozna@gmail.com'
    password = ['qa1023&qa1023', '55555555555']

    with allure.step('Проверка на отображение'):
        check.is_true(page.inp_username.is_visible())
        check.is_true(page.inp_password.is_visible())
        check.is_true(page.btn_come_in.is_visible())

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.btn_come_in.is_clickable())

    with allure.step('Проверка входа с неверным паролем'):
        page.inp_username.send_keys(login)
        page.inp_password.send_keys(password[1])
        page.btn_eye.click()
        page.btn_come_in.click()
        check.equal(page.msg_error.get_text(),'ОШИБКА: введено неверное имя пользователя или пароль. Забыли пароль?')

    with allure.step('Проверка входа с верным паролем'):
        page.inp_username.send_keys(login)
        page.inp_password.send_keys(password[0])
        page.btn_eye.click()
        page.btn_come_in.click()
        check.not_equal(page.msg_successful_registration.get_text().find('Из главной страницы аккаунта вы можете'
                                                                         ' посмотреть ваши недавние заказы'), -1)

