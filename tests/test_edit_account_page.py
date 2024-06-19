import time
import allure
import pytest_check as check
from locators.locators_edit_account_page import EditAccountPage
from locators.locators_my_account_page import MyAccountPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работспособно')
def test_my_account(web_browser):
    """Этот тест еще не дописан"""

    page = MyAccountPage(web_browser)

    with allure.step('Проверка на отображение'):
        check.is_true(page.btn_headers_profile.is_visible())