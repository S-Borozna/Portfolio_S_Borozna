import time
import allure
import pytest_check as check
from locators.locators_main_page import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работоспособности хедера')
def test_main_page_header(web_browser):
    """Этот тест проверяет работоспособность хедера"""

    page = MainPage(web_browser)

    btn_headers = [(page.btn_headers_catalog, 'Каталог товаров', 'https://lakikraski.by/#'),
                   (page.btn_headers_brends, 'Бренды', 'https://lakikraski.by/brands/'),
                   (page.btn_headers_to_help, 'В помощь', 'https://lakikraski.by/#'),
                   (page.btn_headers_about_company, 'О компании', 'https://lakikraski.by/#'),
                   (page.btn_headers_contact, 'Контакты', 'https://lakikraski.by/kontakty-mir-cveta/'),
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
@allure.feature('Тест для проверки выпадающего меню хедера')
def test_v_menu(web_browser):
    """Этот тест проверяет выпадающее меню хедера """

    page = MainPage(web_browser)

    btn_headers = [(page.btn_headers_catalog, page.v_menu_catalog, 5),
                   (page.btn_headers_to_help, page.v_menu_to_help, 5),
                   (page.btn_headers_info, page.v_menu_info, 8),
                   (page.btn_headers_about_company, page.v_menu_about_company, 3)]

    for btn, v_menu, quantity in btn_headers:
        btn.click()

        with allure.step('Проверка на верное количество вкладок в выпадающем меню'):
            x = v_menu.count()
            check.equal(x,quantity)
            btn.click()


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
        check.equal(page.inp_feedback_phone.get_attribute('placeholder'), '+375291234567')
        check.equal(page.inp_feedback_email.get_attribute('placeholder'), 'Ваш Email адрес?')

    with allure.step('Проверка ввода текста и его отображение'):
        test_input = ['Пингвин', '+375298888888', 'penguin@pen.by', 'Вы пингвины?']



        page.inp_feedback_name.send_keys(test_input[0])
        page.inp_feedback_phone.send_keys(test_input[1])
        page.inp_feedback_email.send_keys(test_input[2])
        page.inp_feedback_question.send_keys(test_input[3])

        check.equal(page.inp_feedback_name.get_text(), test_input[0])
        check.equal(page.inp_feedback_phone.get_text(), test_input[1])
        check.equal(page.inp_feedback_email.get_text(), test_input[2])
        check.equal(page.inp_feedback_question.get_text(), test_input[3])

    with allure.step('Проверка работоспособности кнопки "Отправить"'):
        check.is_true(page.btn_feedback_send.is_visible())
        check.is_true(page.btn_feedback_send.is_clickable())
        page.btn_feedback_send.click()
        check.not_equal(page.msg_feedback.get_text().find(f'{test_input[0]} Спасибо за обращение! '
                                                 f'Мы свяжемся с вами в ближайшее время.'),-1)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работоспособности футера')
def test_main_page_footer(web_browser):
    """Этот тест проверяет работоспособность футера"""

    page = MainPage(web_browser)

    btn_footer = [(page.btn_footer_arch_paints, 'Архитектурные краски', 'https://lakikraski.by/product-category/'
                'arhitekturnye-kraski/'),
                  (page.btn_footer_ind_coatings, 'Промышленные покрытия', 'https://lakikraski.by/product-'
                                                                          'category/promyshlennye-pokrytija/'),
                  (page.btn_footer_decor, 'Декоративные материалы', 'https://lakikraski.by/product-category/'
                                                                    'dekorativnye-materialy/'),
                  (page.btn_footer_tools, 'Инструмент', 'https://lakikraski.by/product-category/instrument/'),
                  (page.btn_footer_other_goods, 'Прочие товары', 'https://lakikraski.by/product-category'
                                                                 '/prochie-tovary/'),
                  (page.btn_footer_stock, 'Акции', 'https://lakikraski.by/shop/?yith_wcan=1&onsale_filter=1'),
                  (page.btn_footer_news, 'Новости', 'https://lakikraski.by/news/'),
                  (page.btn_footer_pay_deliver, 'Оплата и доставка', 'https://lakikraski.by/payment-delivery/'),
                  (page.btn_footer_discount, 'Дисконтная программа', 'https://lakikraski.by/discount-program/'),
                  (page.btn_footer_public_offer, 'Публичная оферта', 'https://lakikraski.by/public-offer/'),
                  (page.btn_footer_confident, 'Конфиденциальность', 'https://lakikraski.by/privacy-policy/'),
                  (page.btn_footer_to_buy, 'Где купить?', 'https://lakikraski.by/kontakty-mir-cveta/'),
                  (page.btn_footer_paynt_sistem, 'Системы окраски', 'https://lakikraski.by/sistemy-okraski/'),
                  (page.btn_footer_question, 'Вопрос-ответ', 'https://lakikraski.by/faq/'),
                  (page.btn_footer_expertise, 'Экспертные знания', 'https://lakikraski.by/expertise/'),
                  (page.btn_footer_palettes, 'Палитры цветов', 'https://lakikraski.by/color-palettes/'),
                  (page.btn_footer_brochures, 'Брошюры', 'https://lakikraski.by/brochures/'),
                  (page.btn_footer_contakts, 'Контакты', 'https://lakikraski.by/kontakty-mir-cveta/'),
                  (page.btn_footer_requisites, 'Реквизиты', 'https://lakikraski.by/requisites/'),
                  (page.btn_footer_story, 'История', 'https://lakikraski.by/history/'),
                  (page.btn_footer_vacancies, 'Вакансии', 'https://lakikraski.by/vakansii/'),
                  (page.btn_footer_brands, 'Бренды', 'https://lakikraski.by/brands/'),
                  (page.btn_footer_mc,'','https://lakikraski.by/')]

    for elements, text_elements, href_elements in btn_footer:
        with allure.step('Проверка на отображение'):
            check.is_true(elements.is_visible())

        with allure.step('Проверка на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста {elements}'):
            check.equal(elements.get_text(), text_elements)

        with allure.step(f'Сверка href {elements}'):
            check.equal(elements.get_attribute('href'), href_elements)

