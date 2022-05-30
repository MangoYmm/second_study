import time

from selenium.webdriver.common.by import By

from wechat_contact.base_page.base import base
from wechat_contact.utils.log_util import logger


class AddMemberPage(base):
    # _NAME_INPUT=(By.XPATH,"//*[@placeholder='姓名']")
    # _ACCOUNT_INPUT = (By.ID, "memberAdd_acctid")
    # _MOBILE_PHONE_INPUT = (By.ID,'memberAdd_phone')
    # _BELOW_SAVE_BUTTON =(By.XPATH,'//form/*[@class="member_colRight_operationBar ww_operationBar"][2]/a[text()="保存"]')
    # _SEND_INVITE = (By.XPATH,'//*[@class="member_edit_joinCheckboxCnt member_edit_sec"]//label/*[@class="ww_checkbox"]')
    # _BELOW_SAVE_ADD_BUTTON = (By.XPATH,'//form/*[@class="member_colRight_operationBar ww_operationBar"][2]/a[text()="保存并继续添加"]')
    # _TIPS=(By.ID,"js_tips")

    def add_member_to_contact_page(self,name,account,phone):
        self._NAME_INPUT = self.get_yml_data('_NAME_INPUT')
        self._ACCOUNT_INPUT = self.get_yml_data('_ACCOUNT_INPUT')
        self._MOBILE_PHONE_INPUT = self.get_yml_data('_MOBILE_PHONE_INPUT')
        self._SEND_INVITE = self.get_yml_data('_SEND_INVITE')
        self._BELOW_SAVE_BUTTON = self.get_yml_data('_BELOW_SAVE_BUTTON')

        from wechat_contact.base_page.contact_page import ContactPage
        self.do_send_keys(name,self._NAME_INPUT)
        logger.info("输入姓名成功")
        self.do_send_keys(account,self._ACCOUNT_INPUT)
        logger.info("输入账户成功")
        self.do_send_keys(phone,self._MOBILE_PHONE_INPUT)
        logger.info("输入手机号成功")
        # self.scroll('10','10000')
        self.js_scroll(1000)
        logger.info("滚动页面至底部成功")
        self.do_click(self._SEND_INVITE)
        logger.info("取消发送邀请成功")
        self.do_click(self._BELOW_SAVE_BUTTON)
        logger.info("点击底部的保存按钮成功")
        return ContactPage(self.driver)


    def add_member_again_add(self,name,account,phone):
        self._BELOW_SAVE_ADD_BUTTON = self.get_yml_data('_BELOW_SAVE_ADD_BUTTON')
        self._NAME_INPUT = self.get_yml_data('_NAME_INPUT')
        self._ACCOUNT_INPUT = self.get_yml_data('_ACCOUNT_INPUT')
        self._MOBILE_PHONE_INPUT = self.get_yml_data('_MOBILE_PHONE_INPUT')
        self._SEND_INVITE = self.get_yml_data('_SEND_INVITE')

        from wechat_contact.base_page.contact_page import ContactPage
        self.do_send_keys(name,self._NAME_INPUT)
        logger.info("输入姓名成功")
        self.do_send_keys(account,self._ACCOUNT_INPUT)
        logger.info("输入账户成功")
        self.do_send_keys(phone,self._MOBILE_PHONE_INPUT)
        logger.info("输入手机号成功")
        # self.scroll('10','10000')
        self.js_scroll(1000)
        logger.info("滚动页面至底部成功")
        self.do_click(self._SEND_INVITE)
        logger.info("取消发送邀请成功")
        self.do_click(self._BELOW_SAVE_ADD_BUTTON)
        logger.info("点击底部的保存并继续添加按钮成功")
        time.sleep(8)
        return AddMemberPage(self.driver)


    def get_add_member_name_empty_click_other_tips(self):
        """
        获取  姓名为空时，显示提示语
        :return: 姓名为空，点击其他地方后，输入框右侧显示的提示语
        """
        self._NAME_INPUT = self.get_yml_data('_NAME_INPUT')
        self._ENGLISH_NAME_INPUT = self.get_yml_data('_ENGLISH_NAME_INPUT')
        self._NAME_EMPTY_TIPS = self.get_yml_data('_NAME_EMPTY_TIPS')

        logger.info("点击姓名的输入框")
        self.do_click(self._NAME_INPUT)
        logger.info("点击姓名框后，点击别名输入框")
        self.do_click(self._ENGLISH_NAME_INPUT)
        return self.get_ele_attribute(self._NAME_EMPTY_TIPS)


    def get_add_member_account_empty_click_other_tips(self):
        """
        获取  账户为空时，显示提示语
        :return: 账户为空，点击其他地方后，输入框右侧显示的提示语
        """
        self._ACCOUNT_INPUT = self.get_yml_data('_ACCOUNT_INPUT')
        self._ENGLISH_NAME_INPUT = self.get_yml_data('_ENGLISH_NAME_INPUT')
        self._ACCOUNT_EMPTY_TIPS = self.get_yml_data('_ACCOUNT_EMPTY_TIPS')

        self.do_click(self._ACCOUNT_INPUT)
        logger.info("账户为空，点击别名输入框")
        self.do_click(self._ENGLISH_NAME_INPUT)
        return self.get_ele_attribute(self._ACCOUNT_EMPTY_TIPS)

    def get_add_member_phone_empty_click_other_tips(self):
        """
        获取  手机为空时，显示的提示语
        :return: 手机为空，点击其他地方后，输入框右侧显示的提示语
        """
        self._MOBILE_PHONE_INPUT = self.get_yml_data('_MOBILE_PHONE_INPUT')
        self._ENGLISH_NAME_INPUT = self.get_yml_data('_ENGLISH_NAME_INPUT')
        self._MOBILE_EMPTY_TIPS = self.get_yml_data('_MOBILE_EMPTY_TIPS')

        self.do_click(self._MOBILE_PHONE_INPUT)
        logger.info("点击手机框后，点击别名输入框")
        self.do_click(self._ENGLISH_NAME_INPUT)
        return self.get_ele_attribute(self._MOBILE_EMPTY_TIPS)

    def get_add_member_mail_empty_click_other_tips(self):
        """
        获取  邮箱为空时，显示的提示语
        :return: 邮箱为空，点击其他地方后，邮箱输入框右侧显示的提示语
        """
        self._MAIL_INPUT = self.get_yml_data('_MAIL_INPUT')
        self._ENGLISH_NAME_INPUT = self.get_yml_data('_ENGLISH_NAME_INPUT')
        self._MAIL_EMPTY_TIPS = self.get_yml_data('_MAIL_EMPTY_TIPS')

        self.do_click(self._MAIL_INPUT)
        logger.info("点击邮箱框后，点击别名输入框")
        self.do_click(self._ENGLISH_NAME_INPUT)
        return self.get_ele_attribute(self._MAIL_EMPTY_TIPS)

    def get_tips(self):
        """
        获取提示语
        :return:
        """
        self._TIPS = self.get_yml_data('_TIPS')

        self.wait_until_visibility(self._TIPS)
        return self.get_ele_attribute(self._TIPS)