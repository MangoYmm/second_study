import random
import time
import pytest
from  faker  import  Faker
from wechat_contact.base_page.login_page import LoginPage
from wechat_contact.utils.log_util import logger

class TestAddMember:
    fake = Faker(locale='zh_CN')
    # Faker.seed(4321)
    name = fake.name()
    account = fake.ssn()
    mobile_phone = fake.phone_number()

    login = LoginPage()
    home = login.login_to_home_page()

    add_member_success_tips = login.get_yml_data('add_member_success_tips')
    name_empty_tips_content = login.get_yml_data('_NAME_EMPTY_TIPS_CONTENT')
    account_empty_tips_content = login.get_yml_data('_ACCOUNT_EMPTY_TIPS_CONTENT')
    mobile_empty_tips_content = login.get_yml_data('_MOBILE_EMPTY_TIPS_CONTENT')
    mail_empty_tips_content = login.get_yml_data('_MAIL_EMPTY_TIPS_CONTENT')

    # def teardown_class(self):
    #     self.login.do_quit()

    # @pytest.mark.skip
    def test_add_member_success(self):
        """
        添加成员成功
        :return:
        """
        add_member_back_contact =self.home.goto_contact_page()\
        #     .goto_add_member_page()\
        #     .add_member_to_contact_page(self.name,self.account,self.mobile_phone)
        #
        # member_list = add_member_back_contact.get_member_list()
        # tips = add_member_back_contact.get_tips()
        #
        # logger.info(f"检查刚添加的成员: {self.name} 是否在成员列表: {member_list}中显示")
        # assert self.name in member_list
        #
        # logger.info(f"添加成员成功后弹出的提示为： {tips}")
        # assert tips == self.add_member_success_tips

    @pytest.mark.skip
    def test_add_member_again_add_new(self):
        """t添加成员时，点击保存继续添加成员按钮后，继续添加成员"""
        name1=self.fake.name()
        add_member_page = self.home.goto_contact_page() \
                          .goto_add_member_page()
        add_member_in_add_page = add_member_page.add_member_again_add(name1, self.fake.ssn(), self.fake.phone_number())

        name2 = self.fake.name()
        member_list = add_member_in_add_page.add_member_to_contact_page(name2, self.fake.ssn(), self.fake.phone_number())\
            .get_member_list()

        logger.info(f"检查刚添加的成员: {name1}、{name2} 是否在成员列表: {member_list}中显示")
        assert all( name in member_list for name in [name1,name2])



    @pytest.mark.skip
    def test_add_member_again_add_exist(self):
        """添加存在的成员"""
        add_member_back_contact =self.home.goto_contact_page()\
            .goto_add_member_page()\
            .add_member_again_add(self.name,self.account,self.mobile_phone)\
            .add_member_to_contact_page(self.name,self.account,self.mobile_phone)

        exist_account_tips = add_member_back_contact.get_add_member_exist_account_tips()
        exist_mail_tips = add_member_back_contact.get_add_member_exist_mail_tips()
        exist_mobile_tips = add_member_back_contact.get_add_member_exist_mobile_tips()

        logger.info(f"添加成员输入账户是已存在的，页面显示的提示为： {exist_account_tips}")
        assert exist_account_tips == f'该帐号已被“{self.name}”占有'

        logger.info(f"添加成员输入邮箱是已存在的，页面显示的提示为： {exist_mail_tips}")
        assert exist_mail_tips == f'该企业邮箱已被“{self.name}”占有'

        logger.info(f"添加成员输入手机是已存在的，页面显示的提示为： {exist_mobile_tips}")
        assert exist_mobile_tips == f'该手机已被“{self.name}”占有'

    @pytest.mark.skip
    def test_add_member_check_required(self):
        """检查姓名、企业邮箱、手机号的必填项"""
        add_member_page = self.home.goto_contact_page() \
            .goto_add_member_page()
        logger.info("断言 姓名为空，是否有显示提示语")
        assert  add_member_page.get_add_member_name_empty_click_other_tips() == self.name_empty_tips_content

        assert add_member_page.get_add_member_account_empty_click_other_tips() == self.account_empty_tips_content

        assert add_member_page.get_add_member_phone_empty_click_other_tips() == self.mobile_empty_tips_content

        assert add_member_page.get_add_member_mail_empty_click_other_tips() == self.mail_empty_tips_content

