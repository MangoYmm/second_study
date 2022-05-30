import os
import time
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from wechat_contact.utils.get_cookies import get_cookies
from wechat_contact.utils.log_util import logger

os.environ['BROWSER_TYPE']='firefox'

class base:
    """与driver交互"""
    _BASE_URL = ""
    def __init__(self,base_driver:WebDriver=None):
        if base_driver is None:
            if os.environ.get('BROWSER_TYPE') == 'google':
                self.driver = webdriver.Chrome()
            elif os.environ.get('BROWSER_TYPE') == 'firefox':
                self.driver = webdriver.Firefox()

            self.driver.maximize_window()
            self.driver.implicitly_wait(8)
            """
            url = 'https://work.weixin.qq.com/wework_admin/frame'
            options = Options()
            options.add_experimental_option('w3c',False)
            options.debugger_address = 'localhost:9222'
            self.driver = webdriver.Chrome(options=options)
            # self.driver.maximize_window()
            self.driver.get(url)
            """
        else:
            self.driver = base_driver

        # if not self.driver.current_url.startswith('https'):
        #     self.driver.get(self._BASE_URL)

    by_map={"XPATH":By.XPATH,
            "ID":By.ID,
            "CLASS_NAME":By.CLASS_NAME,
            "CSS_SELECTOR":By.CSS_SELECTOR}

    def get_yml_data(self,element_name):
        """
        获取data.yml中的数据
        :param element_name: 指定获取某个数据，可以是某个元素的名称，或者某个url的名称
        :return:
        """
        ph = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(ph + '\datas\data.yml', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        data = datas[element_name]
        if isinstance(data,dict):
            return (self.by_map.get(data['by'].upper()),data['locator'])
        else:
            return data


    def do_find(self,by,locator=None):
        """获取一个元素"""
        if isinstance(by,tuple):
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by,locator)
        #或者判断locator是否为None
        # if locator is None:
        #     return self.driver.find_element(*by)
        # else:
        #     return self.driver.find_element(by,locator)

    def do_click(self,by,locator=None):
        """找到元素后进行点击"""
        self.do_find(by,locator).click()

    def do_send_keys(self,input,by,locator=None):
        """
        找到元素后进行输入
        :param input: 输入的字符串
        :param by: 定位元素的方式，比如By.XPATH，也支持元组格式
        :param locator: 元素在dom树种的位置
        :return:
        """
        ele = self.do_find(by,locator)
        ele.clear()
        ele.send_keys(input)

    def do_eles(self, by, locator=None):
        """获取一组元素"""
        #判断locator是否为None
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by,locator)

    def wait_until_clickable_click(self,by:tuple,timeout=10):
        """等待元素可点击后进行点击"""
        WebDriverWait(self.driver,timeout=timeout).until(expected_conditions.element_to_be_clickable(by)).click()

    def wait_until_visibility(self,by:tuple,timeout=10):
        """等待元素可见"""
        return WebDriverWait(self.driver,timeout=timeout).until(expected_conditions.visibility_of_element_located(by))

    def wait_until_visibility_click(self,by:tuple,timeout=10):
        """等待元素可见后点击"""
        self.wait_until_visibility(by,timeout).click()

    def repeat_click_until_success(self, source_ele_by:tuple, target_ele_by:tuple, times=5):
        """
        点击多次直到点击成功，点击成功的标志就是目标元素出现了
        :param source_ele_by: 点击的源元素
        :param target_ele_by: 点击成功后，应该可见的目标元素
        :param times: 点击次数，默认是5次
        :return:
        """
        count = 0
        while count<times:
            time.sleep(1)
            count += 1
            try:
                self.do_click(source_ele_by)
                logger.info(f'第{count}次时点击成功了')
                self.wait_until_visibility_click(target_ele_by)
                logger.info(f'第{count}次目标元素时可见了')
                break
            except Exception:
                logger.info(f'第{count}次点击异常')

    def scroll(self,xoffset:str, yoffset:str):
        """
        滚动页面
        :param xoffset: 距离x轴的距离
        :param yoffset: 距离y轴的距离
        :return:
        """
        TouchActions(self.driver).scroll(xoffset,yoffset).perform()

    def js_scroll(self,scrollTop:int):
        """
        上下滚动页面
        :param scrollTop: 距离页面上边界的距离
        :return:
        """
        self.driver.execute_script(f'document.documentElement.scrollTop={scrollTop}')

    def get_ele_attribute(self,by,locator=None,attr_name=None):
        """
        获取一个元素的属性
        :param by: 定位元素的方式
        :param locator:
        :param attr_name: 属性名，如果不传该参数，就默认去获取元素的text
        :return:
        """
        if attr_name is None:
            return self.do_find(by,locator).text
        else:
            return self.do_find(by,locator).get_attribute(attr_name)

    def get_eles_attribute(self,by,locator=None,attr_name=None):
        """
        获取一组元素的属性
        :param by:
        :param locator:
        :param attr_name: 属性名，如果不传该参数，就默认去获取元素的text
        :return:
        """
        if attr_name is None:
            return [ele.text for ele in self.do_eles(by, locator)]
        else:
            return [ele.get_attribute(attr_name) for ele in self.do_eles(by,locator)]

    def do_quit(self):
        self.driver.quit()