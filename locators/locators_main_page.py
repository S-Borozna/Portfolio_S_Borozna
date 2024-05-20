import os

from Portfolio_S_Borozna.page.base_page import WebPage
from Portfolio_S_Borozna.page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://lakikraski.by/'

        super().__init__(web_driver, url)

    btn_headers_mc = WebElement(xpath='(//*[@alt="Мир Цвета логотип фотография изображение картинка"])[1]')
    headers_search = WebElement(xpath='(//*[@aria-label="Search input"])[1]')
    btn_headers_feedback = WebElement(xpath='(//*[@data-widget_type="button.default"])[1]//a')
    btn_headers_catalog = WebElement(xpath='((//*[@data-widget_type="ekit-vertical-menu.default"])[1]//a)[1]')
    btn_headers_brends = WebElement(xpath='((//*[@data-widget_type="nav-menu.default"])[1]//a)[1]')
    btn_headers_to_help = WebElement (xpath = '(//*[@aria-haspopup="true"])[1]')
    btn_headers_about_company = WebElement (xpath = '((//*[@data-widget_type="nav-menu.default"])[1]//'
                                                    '*[@aria-expanded="false"])[7]')
    btn_headers_contact = WebElement (xpath = '((//*[@data-widget_type="nav-menu.default"])[1]//a)[23]')

