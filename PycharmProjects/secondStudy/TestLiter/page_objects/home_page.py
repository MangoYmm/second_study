import time
from selenium.webdriver.common.by import By
from utils.log_utils import logger
from secondStudy.TestLiter.utils.log_utils import logger
from page_objects.base_page import Base
from page_objects.category_page import Category_Page
from secondStudy.TestLiter.utils.web_utils import exception_save


class Home_Page(Base):
    __PRODUCT_MANAGER = (By.XPATH, '//div[@class="el-submenu__title"]/span[text()="商场管理"]')
    __PRODUCT_CATEGORY = (By.XPATH, '//*[contains(@class,"is-opened")]//li[@role="menuitem"]/span[text()="商品类目"]')

    @exception_save
    def goto_category_page(self):
        # 点击商场管理
        logger.info("点击商场管理")
        # self.driver.find_element(By.XPATH, '//div[@class="el-submenu__title"]/span[text()="商场管理"]').click()
        self.multi_click_until_find(self.__PRODUCT_MANAGER,self.__PRODUCT_CATEGORY)
        time.sleep(2)
        # 点击商品类目
        logger.debug("点击商品类目")
        # self.driver.find_element(By.XPATH, '//li[@role="menuitem"]/span[text()="商品类目"]').click()
        self.do_find_click(self.__PRODUCT_CATEGORY)
        return Category_Page(self.driver)