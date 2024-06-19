import os

from page.base_page import WebPage
from page.elements import WebElement


class EditAccountPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://lakikraski.by/my-account/edit-account/'

        super().__init__(web_driver, url)

    inp_ac_detail_firstname = WebElement(xpath='//*[@name="account_first_name"]')
    inp_ac_detail_lastname = WebElement(xpath='//*[@name="account_last_name"]')
    inp_ac_detail_displayname = WebElement(xpath='//*[@name="account_display_name"]')
    btn_ac_detail_save = WebElement(xpath='//*[@name="save_account_details"]')