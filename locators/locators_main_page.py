import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://lakikraski.by/'

        super().__init__(web_driver, url)

    btn_headers_mc = WebElement(xpath='(//*[@data-widget_type="image.default"])[1]//a')
    headers_search = WebElement(xpath='(//*[@aria-label="Search input"])[1]')
    btn_headers_feedback = WebElement(xpath='(//*[@data-widget_type="button.default"])[1]//a')
    btn_headers_catalog = WebElement(xpath='((//*[@data-widget_type="ekit-vertical-menu.default"])[1]//a)[1]')
    btn_headers_brends = WebElement(xpath='((//*[@data-widget_type="nav-menu.default"])[1]//a)[1]')
    btn_headers_info = WebElement(xpath='((//*[@data-widget_type="nav-menu.default"])[1]//*'
                                        '[@aria-expanded="false"])[5]')
    btn_headers_to_help = WebElement(xpath='(//*[@aria-haspopup="true"])[1]')
    btn_headers_about_company = WebElement(xpath='((//*[@data-widget_type="nav-menu.default"])[1]//'
                                                 '*[@aria-expanded="false"])[7]')
    btn_headers_contact = WebElement(xpath='((//*[@data-widget_type="nav-menu.default"])[1]//a)[23]')
    btn_headers_basket = WebElement(xpath='(//*[@data-widget_type="woocommerce-menu-cart.default"])[1]//*'
                                          '[@aria-expanded="false"]')
    btn_headers_profile = WebElement(xpath='(//*[@title="Мой аккаунт"])[1]')
    btn_footer_arch_paints = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[6]')
    btn_footer_ind_coatings = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[7]')
    btn_footer_decor = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[8]')
    btn_footer_tools = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[9]')
    btn_footer_other_goods = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[10]')
    btn_footer_stock = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[11]')
    btn_footer_news = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[12]')
    btn_footer_pay_deliver = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[13]')
    btn_footer_discount = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[14]')
    btn_footer_public_offer = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[15]')
    btn_footer_confident = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[16]')
    btn_footer_to_buy = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[17]')
    btn_footer_paynt_sistem = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[18]')
    btn_footer_question = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[19]')
    btn_footer_expertise = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[20]')
    btn_footer_palettes = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[21]')
    btn_footer_brochures = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[22]')
    btn_footer_contakts = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[23]')
    btn_footer_requisites = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[24]')
    btn_footer_story = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[25]')
    btn_footer_vacancies = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[26]')
    btn_footer_brands = WebElement(xpath='(//*[@data-elementor-type="footer"]/*[2]//a)[27]')
    btn_footer_mc = WebElement(xpath='(//*[@data-widget_type="image.default"])[4]//a')
    result_search = WebElement(xpath=' (//div[@class="asp_results_top"])[3]')
    inp_feedback_name = WebElement(xpath='(//*[@aria-modal="true"]//*[@aria-invalid="false"])[1]')
    inp_feedback_phone = WebElement(xpath='(//*[@aria-modal="true"]//*[@aria-invalid="false"])[2]')
    inp_feedback_email = WebElement(xpath='(//*[@aria-modal="true"]//*[@aria-required="false"])[1]')
    inp_feedback_question = WebElement(xpath='(//*[@aria-modal="true"]//*[@aria-required="false"])[2]')
    btn_feedback_send = WebElement(xpath='//*[@aria-modal="true"]//button')
    msg_feedback = WebElement(xpath='//pre')
    v_menu_catalog = ManyWebElements(xpath='(//*[@id="menu-vertikalnoe-menju"])[2]/*')
    v_menu_to_help = ManyWebElements(xpath='(//*[@aria-expanded="false"])[2]/*')
    v_menu_info = ManyWebElements(xpath='(//*[@aria-expanded="false"])[6]/*')
    v_menu_about_company = ManyWebElements(xpath='(//*[@aria-expanded="false"])[8]/*')
    btn_slider_1_rigt = WebElement(xpath='(//*[@aria-label="Next slide"])[1]//*[@aria-hidden="true"]')
    btn_slider_1_left = WebElement(xpath='(//*[@aria-label="Previous slide"])[1]//*[@aria-hidden="true"]')
    btn_slider_2_rigt = WebElement(xpath='(//*[@aria-label="Next slide"])[2]//*[@aria-hidden="true"]')
    btn_slider_2_left = WebElement(xpath='(//*[@aria-label="Previous slide"])[2]//*[@aria-hidden="true"]')