from selenium.webdriver.common.by import By

from wechat_contact.base_page.base import base
from wechat_contact.utils.log_util import logger


class AddDepartmentPage(base):
    # _DEPARTMENT_NAME_INPUT=(By.XPATH,'//label[text()="部门名称"]/../input')
    # _CHOOSE_BELONG_DEPARTMNET_BUTTON=(By.XPATH,'//label[text()="所属部门"]/../a')
    # _CHOOSE_FIRST_LEVEL_DEPARTMENT =(By.XPATH,'//*[@class="qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container"]//*[@aria-level="1"]/a')
    # _CHOOSE_SECOND_LEVEL_DEPARTMENT =(By.XPATH,'//*[@class="qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container"]//*[@aria-level="2"]/a')
    # _CONFIRM_BUTTON=(By.XPATH,'//*[text()="确定"]')
    def add_department_to_contact_page(self,name,parent_level):
        self._DEPARTMENT_NAME_INPUT = self.get_yml_data('_DEPARTMENT_NAME_INPUT')
        self._CHOOSE_BELONG_DEPARTMNET_BUTTON = self.get_yml_data('_CHOOSE_BELONG_DEPARTMNET_BUTTON')
        self._CHOOSE_FIRST_LEVEL_DEPARTMENT = self.get_yml_data('_CHOOSE_FIRST_LEVEL_DEPARTMENT')
        self._CHOOSE_SECOND_LEVEL_DEPARTMENT = self.get_yml_data('_CHOOSE_SECOND_LEVEL_DEPARTMENT')
        self._CONFIRM_BUTTON = self.get_yml_data('_CONFIRM_BUTTON')

        from wechat_contact.base_page.contact_page import ContactPage
        logger.info("输入部门名称")
        self.do_send_keys(name,self._DEPARTMENT_NAME_INPUT)
        logger.info("点击所属部门框，展示部门的下拉框")
        self.do_click(self._CHOOSE_BELONG_DEPARTMNET_BUTTON)
        if parent_level== 1:
            logger.info("点击第一层级的部门")
            self.do_click(self._CHOOSE_FIRST_LEVEL_DEPARTMENT)
        elif parent_level== 2:
            logger.info("点击第二层级的部门")
            self.do_click(self._CHOOSE_SECOND_LEVEL_DEPARTMENT)
        logger.info("点击保存按钮")
        self.do_click(self._CONFIRM_BUTTON)
        return ContactPage(self.driver)