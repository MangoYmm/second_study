import os

import yaml
from wechat_contact.base_page.base import base
from wechat_contact.base_page.home_page import HomePage
from wechat_contact.utils.log_util import logger


class LoginPage(base):
    # _BASE_URL = 'https://work.weixin.qq.com/wework_admin/frame'

    def login_to_home_page(self):
        self._BASE_URL = self.get_yml_data('_BASE_URL')

        self.driver.get(self._BASE_URL)
        with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'datas\cookies.yml'),
                  encoding='utf-8') as f:
            logger.info('获取yml的cookie')
            cookies = yaml.safe_load(f)

        logger.info('文件中的cookie添加到当前driver中')
        for i in cookies:
            self.driver.add_cookie(i)

        self.driver.get(self._BASE_URL)

        return HomePage(self.driver)