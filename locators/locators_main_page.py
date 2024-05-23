import os

from Portfolio_S_Borozna.page.base_page import WebPage
from Portfolio_S_Borozna.page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://hoster.by/'

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
    btn_headers_basket = WebElement (xpath = '(//*[@data-widget_type="woocommerce-menu-cart.default"])[1]//i')
    btn_headers_profile = WebElement (xpath = '(//*[@data-widget_type="icon.default"])[1]//*[@aria-hidden="true"]')
    btn_footer_arch_paints = WebElement (xpath = '(//*[@data-elementor-type="footer"]/*[2]//span)[8]')
    btn_footer_ind_coatings = WebElement (xpath = '(//*[@data-elementor-type="footer"]/*[2]//span)[9]')
    btn_footer_decor = WebElement (xpath = '(//*[@data-elementor-type="footer"]/*[2]//span)[10]')
    btn_footer_tools = WebElement (xpath = '(//*[@data-elementor-type="footer"]/*[2]//span)[11]')
    hed_search = WebElement(xpath = '//*[@placeholder="Введите домены"]')
    btn_search = WebElement(xpath ="(//*[contains(concat(' ', normalize-space(@class), ' '), ' m-button ')])[6]")
    txt1 = WebElement (xpath = '((//*[@aria-hidden="false"])[1]//span)[8]')
    txt2 = WebElement (xpath = '(//section//div)[11]')
    var_dom = WebElement (xpath = '(//*[@name="choosedzones"])[1]/*[1]')
    rez = WebElement (xpath = '(//*[@aria-hidden="false"])[1]')

