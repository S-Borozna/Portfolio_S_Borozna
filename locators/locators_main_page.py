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
    btn_headers_to_help = WebElement(xpath='(//*[@aria-haspopup="true"])[1]')
    btn_headers_about_company = WebElement(xpath='((//*[@data-widget_type="nav-menu.default"])[1]//'
                                                 '*[@aria-expanded="false"])[7]')
    btn_headers_contact = WebElement(xpath='((//*[@data-widget_type="nav-menu.default"])[1]//a)[23]')
    btn_headers_basket = WebElement(xpath='(//*[@data-widget_type="woocommerce-menu-cart.default"])[1]//i')
    btn_headers_profile = WebElement(xpath='(//*[@data-widget_type="icon.default"])[1]//*[@aria-hidden="true"]')
    btn_footer_arch_paints = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[8]')
    btn_footer_ind_coatings = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[9]')
    btn_footer_decor = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[10]')
    btn_footer_tools = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[11]')
    btn_footer_other_goods = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[12]')
    btn_footer_stock = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[15]')
    btn_footer_news = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[16]')
    btn_footer_pay_deliver = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[17]')
    btn_footer_discount = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[18]')
    btn_footer_public_offer = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[19]')
    btn_footer_confident = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[20]')
    btn_footer_to_buy = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[21]')
    btn_footer_paynt_sistem = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[24]')
    btn_footer_question = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[25]')
    btn_footer_expertise = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[26]')
    btn_footer_palettes = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[27]')
    btn_footer_brochures = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[28]')
    btn_footer_contakts = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[31]')
    btn_footer_requisites = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[32]')
    btn_footer_story = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[33]')
    btn_footer_vacancies = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[34]')
    btn_footer_brands = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//span)[35]')
    btn_footer_mc = WebElement(xpath='(//*[@alt="worldofcolor-white-slogan-logo"])[2]')
    result_search = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), "
                                     "' asp_results_top ')])[3]")
    inp_feedback_name = WebElement(xpath='(//*[@aria-modal="true"]//*[@aria-invalid="false"])[1]')
    inp_feedback_phone = WebElement(xpath='(//*[@aria-modal="true"]//*[@aria-invalid="false"])[2]')
    inp_feedback_email = WebElement(xpath='(//*[@aria-modal="true"]//*[@aria-required="false"])[1]')
    inp_feedback_question = WebElement(xpath='(//*[@aria-modal="true"]//*[@aria-required="false"])[2]')
    btn_feedback_send = WebElement(xpath='//*[@aria-modal="true"]//button')
