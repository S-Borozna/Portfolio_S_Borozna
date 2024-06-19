import os

from page.base_page import WebPage
from page.elements import WebElement


class MyAccountPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://lakikraski.by/my-account/'

        super().__init__(web_driver, url)

    inp_email_registration = WebElement(xpath='(//*[@name="email"])[1]')
    btn_registration = WebElement(xpath='//*[@name="register"]')
    msg_error = WebElement(xpath='//*[@role="alert"]')
    msg_successful_registration = WebElement(xpath="//*[contains(concat(' ', normalize-space(@class), ' '), "
                                                   "' woocommerce-MyAccount-content-wrapper ')]")
    inp_username = WebElement(xpath='//*[@name="username"]')
    inp_password = WebElement(xpath='//*[@name="password"]')
    btn_come_in = WebElement(xpath='//*[@name="login"]')
    btn_replace_me = WebElement(xpath='(//*[@data-widget_type="woocommerce-my-account.default"]//label)[3]')
    btn_control_panel = WebElement(xpath='(//*[@data-widget_type="woocommerce-my-account.default"]//a)[1]')
    btn_orders = WebElement(xpath='(//*[@data-widget_type="woocommerce-my-account.default"]//a)[2]')
    btn_addresses = WebElement(xpath='(//*[@data-widget_type="woocommerce-my-account.default"]//a)[4]')
    btn_account_details = WebElement(xpath='(//*[@data-widget_type="woocommerce-my-account.default"]//a)[5]')
    btn_exit = WebElement(xpath='(//*[@data-widget_type="woocommerce-my-account.default"]//a)[6]')
