from selenium.webdriver.common.by import By

from wechat_contact.base_page.add_department_page import AddDepartmentPage
from wechat_contact.base_page.add_member_page import AddMemberPage
from wechat_contact.base_page.base import base
from wechat_contact.utils.log_util import logger


class ContactPage(base):
    # _ADD_MEMBER_BUTTON=(By.XPATH,'//div[@class="js_has_member"]/div[1]/a[text()="添加成员"]')
    # _ADD_BUTTON=(By.CSS_SELECTOR,'.member_colLeft_top_addBtn')
    # _ADD_DEPARTMENT_BUTTON=(By.CSS_SELECTOR,'.vakata-context.jstree-contextmenu.jstree-default-contextmenu.js_create_dropdown_container>li:nth-child(1)>a')
    # _MEMBER_NAME_LIST=(By.XPATH,'//*[@id="member_list"]/tr/td[2]/span')
    # _INVITE_BUTTON= (By.XPATH,'//*[@class="js_list_warn js_unactive_warn ww_fixedTip member_fixedTip"]//*[text()="立即邀请"]')
    # _NAME_INPUT = (By.XPATH, "//*[@placeholder='姓名']")
    # _TIPS=(By.ID,"js_tips")
    #
    # _DEPARTMENT_NAME_LIST=(By.XPATH,'//*[@role="treeitem"]//a')
    # _LEVEL_2_FIRST_DEPARTMNET=(By.XPATH,'//*[@role="treeitem"]//li[@aria-level="2"][1]/a')
    # _ANY_LEVEL_3_DEPARTMNET=(By.XPATH,'//*[@aria-level="3"]')
    #
    # _ACCOUNT_EXIST_TIPS=(By.XPATH,'//*[@id="memberAdd_acctid"]/../div')
    # _MAIL_EXIST_TIPS=(By.XPATH,'//*[@id="memberAdd_biz_mail"]/../div')
    # _MOBILE_EXIST_TIPS=(By.XPATH,'//*[@class="ww_telInput"]/../div[@class="ww_inputWithTips_tips"]')

    def goto_add_member_page(self):
        # self.wait_until_clickable_click(self._ADD_MEMBER_BUTTON,timeout=30)
        self._ADD_MEMBER_BUTTON=self.get_yml_data('_ADD_MEMBER_BUTTON')
        self._NAME_INPUT = self.get_yml_data('_NAME_INPUT')

        logger.info("点击添加成员按钮")
        self.repeat_click_until_success(self._ADD_MEMBER_BUTTON, self._NAME_INPUT, 20)
        return AddMemberPage(self.driver)

    def goto_add_department_page(self):
        self._ADD_BUTTON = self.get_yml_data('_ADD_BUTTON')
        self._ADD_DEPARTMENT_BUTTON = self.get_yml_data('_ADD_DEPARTMENT_BUTTON')

        logger.info("点击添加加号按钮")
        self.wait_until_clickable_click(self._ADD_BUTTON,20)
        logger.info("点击添加部门按钮")
        self.do_click(self._ADD_DEPARTMENT_BUTTON)
        return AddDepartmentPage(self.driver)

    def get_tips(self):
        """
        获取添加成员或部门后弹出的冒泡提示语
        :return:
        """
        self._TIPS = self.get_yml_data('_TIPS')

        self.wait_until_visibility(self._TIPS)
        return self.get_ele_attribute(self._TIPS)

    def get_member_list(self):
        """
        :return: 获取通讯录页的所有的成员的姓名
        """
        self._INVITE_BUTTON = self.get_yml_data('_INVITE_BUTTON')
        self._MEMBER_NAME_LIST = self.get_yml_data('_MEMBER_NAME_LIST')

        self.wait_until_visibility(self._INVITE_BUTTON)
        return self.get_eles_attribute(self._MEMBER_NAME_LIST)

    def get_default_level_department_list(self):
        """
        :return: 获取通讯录页的第1层级和第2层级的部门的名称
        """
        self._DEPARTMENT_NAME_LIST = self.get_yml_data('_DEPARTMENT_NAME_LIST')
        self._TIPS = self.get_yml_data('_TIPS')

        self.wait_until_visibility(self._TIPS)
        return self.get_eles_attribute(self._DEPARTMENT_NAME_LIST)

    def get_level_3_department_list(self):
        """
        :return: 获取通讯录页的第1层级、第2层级以及点击的第2层级的子部门的名称
        """
        self._TIPS = self.get_yml_data('_TIPS')
        self._LEVEL_2_FIRST_DEPARTMNET = self.get_yml_data('_LEVEL_2_FIRST_DEPARTMNET')
        self._ANY_LEVEL_3_DEPARTMNET = self.get_yml_data('_ANY_LEVEL_3_DEPARTMNET')
        self._DEPARTMENT_NAME_LIST = self.get_yml_data('_DEPARTMENT_NAME_LIST')

        self.wait_until_visibility(self._TIPS)
        self.do_click(self._LEVEL_2_FIRST_DEPARTMNET)
        self.wait_until_visibility(self._ANY_LEVEL_3_DEPARTMNET)
        return self.get_eles_attribute(self._DEPARTMENT_NAME_LIST)

    def get_add_member_exist_account_tips(self):
        """获取 添加成员输入已存在的账户时，页面显示的提示语"""
        self._ACCOUNT_EXIST_TIPS = self.get_yml_data('_ACCOUNT_EXIST_TIPS')

        return self.get_ele_attribute(self._ACCOUNT_EXIST_TIPS)

    def get_add_member_exist_mail_tips(self):
        """获取 添加成员输入已存在的邮箱时，页面显示的提示语"""
        self._MAIL_EXIST_TIPS = self.get_yml_data('_MAIL_EXIST_TIPS')

        return self.get_ele_attribute(self._MAIL_EXIST_TIPS)

    def get_add_member_exist_mobile_tips(self):
        """获取 添加成员输入已存在的手机号时，页面显示的提示语"""
        self._MOBILE_EXIST_TIPS = self.get_yml_data('_MOBILE_EXIST_TIPS')

        return self.get_ele_attribute(self._MOBILE_EXIST_TIPS)