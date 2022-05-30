from selenium.webdriver.common.by import By
from wechat_contact.base_page.base import base
from wechat_contact.base_page.contact_page import ContactPage
from wechat_contact.utils.log_util import logger


class HomePage(base):
    # _CONTACT_ELE =(By.XPATH,'//*[@id="menu_contacts"]')
    def goto_contact_page(self):
        self._CONTACT_ELE = self.get_yml_data('_CONTACT_ELE')

        logger.info("点击通讯录按钮")
        self.do_click(self._CONTACT_ELE)

        return ContactPage(self.driver)