import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest  import *
from selenium.webdriver.support.wait import WebDriverWait

class TestAppium:

    def setup(self):
        desired_caps = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "platformVersion":'6.0',
        "deviceName": "127.0.0.1:7555",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "noReset":"True",
        "adbExecTimeout":200000
        # "newCommandTimeout":60000
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        pass
    #,('小米','01810',26.35)
    @pytest.mark.parametrize('text,codenum,expectprice',[('阿里巴巴','09988',193.5)])
    def  test_input(self,text,codenum,expectprice):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys(text)
        #el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
        el3=self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/listview']/*[@class='android.widget.RelativeLayout'][1]")
        el3.click()
        price=self.driver.find_element_by_xpath(f"//*[@text='{codenum}']/../../../*[@resource-id='com.xueqiu.android:id/price_layout']/*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert expectprice==float(price)
        self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
        # self.driver.find_element_by_accessibility_id("123")
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"123").get_attribute('')
#     def test_touchaction(self):
#         #获取窗口的坐标
#         window_rect=self.driver.get_window_rect()
#         width=window_rect['width']
#         height = window_rect['height']
#         TouchAction(self.driver).press(x=width*0.5, y=height*0.2).wait(200).move_to(x=width*0.5, y=height*0.4).release().perform()
#         #TouchAction(self.driver).press(x=299,y=969).wait(200).move_to(x=299,y=300).release().perform()
#     def test_uiauto(self):
#         self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
#         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("我的")').click()
#         #组合定位
#         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("我的")。text("123")').click()
#     # def test_scroll_find_element(self):
    #     #实现滚动找元素
    #     self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).')
    #     self.driver.page_source()
    @pytest.mark.skip("跳过测试")
    def test_get_attribute(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(el1.get_attribute("text"))
        assert  "搜索股票"  in  el1.get_attribute("text")
        print(el1.get_attribute("resource-id"))
        print(el1.get_attribute("enabled"))
        print(el1.get_attribute("checkable"))

    @pytest.mark.skip("跳过测试")
    def test_assert(self):
        a=10
        b=20
        assert  a<b

    @pytest.mark.skip("跳过测试")
    def test_hamcrest(self):
        assert_that(10,equal_to(10),"这是一个提示信息")
        assert_that(10,close_to(9,1))
        assert_that("contains some strings",contains_string("some"))


















