import random
import time

import pytest
from wechat_contact.base_page.home_page import HomePage
from  faker  import  Faker
from wechat_contact.base_page.login_page import LoginPage
from wechat_contact.utils.log_util import logger

class TestAddDepartmnet:
    fake = Faker(locale='zh_CN')
    fake.random.seed()
    name = fake.name()
    account = fake.ssn()
    mobile_phone = fake.phone_number()
    login = LoginPage()
    home = login.login_to_home_page()

    add_departmnet_success_tips = login.get_yml_data('add_departmnet_success_tips')
    add_exist_department_tips = login.get_yml_data('add_exist_department_tips')

    def teardown_class(self):
        self.login.do_quit()

    # @pytest.mark.skip
    def test_add_departmnet_parentLevel_1(self):
        """检查 添加1级部门的子部门 可以成功"""
        name = '部门'+str(random.randint(1,100))
        add_department_back_contact= self.home.goto_contact_page()\
            .goto_add_department_page()\
            .add_department_to_contact_page(name,1)
        department_list = add_department_back_contact.get_default_level_department_list()
        tips = add_department_back_contact.get_tips()
        logger.info(f"检查刚添加的部门: {name} 是否在部门列表: {department_list}中显示")
        assert name in department_list
        logger.info(f"添加部门成功后弹出的提示为： {tips}")
        assert tips == self.add_departmnet_success_tips

    # @pytest.mark.skip
    def test_add_departmnet_parentLevel_2(self):
        """检查 添加2级部门的子部门 可以成功"""
        name = self.name+'部门'+str(random.randint(1,100))
        add_department_back_contact= self.home.goto_contact_page()\
            .goto_add_department_page()\
            .add_department_to_contact_page(name,2)
        department_list = add_department_back_contact.get_level_3_department_list()
        tips = add_department_back_contact.get_tips()
        logger.info(f"检查刚添加的部门: {name} 是否在部门列表: {department_list}中显示")
        assert name in department_list
        logger.info(f"添加部门成功后弹出的提示为： {tips}")
        assert tips == self.add_departmnet_success_tips

    # @pytest.mark.skip
    def test_add_exist_department(self):
        """检查添加已存在的部门，预期会弹出提示语： 该部门已存在"""
        name = '部门'+str(random.randint(1,100))
        contact_page= self.home.goto_contact_page()
        contact_page.goto_add_department_page()\
            .add_department_to_contact_page(name,1)
        time.sleep(8)
        add_exist_tips = contact_page.goto_add_department_page()\
            .add_department_to_contact_page(name,1).get_tips()
        logger.info(f"添加存在的部门后弹出的提示为： {add_exist_tips}")
        assert add_exist_tips == self.add_exist_department_tips