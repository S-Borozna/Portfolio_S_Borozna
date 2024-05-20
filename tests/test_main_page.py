import pytest_check as check
from Portfolio_S_Borozna.locators.locators_main_page import MainPage


def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)


    check.equal(page.btn_headers_domain.get_text(), 'Домены', 'Тест локатора не равен ожидаймому результату')
    check.is_true(page.btn_headers_mail.is_visible())
