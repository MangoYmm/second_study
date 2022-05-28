import time

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

class TestAppiumWeixin:
	def setup(self):
		desired_caps = {
			"platformName": "Android",
			"platformVersion": "6.0",
			#"deviceName": "192.168.18.101:5555",
			"deviceName": "127.0.0.1:7555",
			"appPackage": "com.tencent.wework",
			"appActivity": ".launch.LaunchSplashActivity",
			"chromedriverExecutable": "D:/DownloadTools/chromedriver74_win32/chromedriver.exe",
			# "chromedriverExecutableDir": "D:/DownloadTools/chromedriver_win32",
			"noReset": "True",
			"skipDeviceInitialization": "true"
			# "adbExecTimeout":200000
			# "newCommandTimeout":60000
		}
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(30)

	def teardown(self):
		pass

	def swipe_find(self,text,num):
		for i in range(num):
			try:
				# 点击添加成员
				element=self.driver.find_element_by_xpath(f'//*[@text="{text}"]')
				self.driver.implicitly_wait(5)
				return  element
			except:
				print("没找到")
				wind=self.driver.get_window_size()
				print(wind)
				height=wind["height"]
				width = wind["width"]
				start_x = width*0.6
				start_y = height*0.8
				end_x=start_x
				end_y=height*0.3
				self.driver.swipe(start_x,start_y,end_x,end_y,2000)
				self.driver.implicitly_wait(5)
			if i ==num-1:
				raise NoSuchElementException(f"找到了{i},没找到")


	def test_webview_Weixin(self):
		f = Faker(locale='zh_CN')
		name = f.name()
		telephone = f.phone_number()
		# 点击通讯录
		self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
		# 点击添加成员
		#self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
		self.swipe_find("添加成员",3).click()
		#滚动查找添加成员按钮
		#self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
		# 点击手动输入添加
		WebDriverWait(self.driver, 30).until(
			expected_conditions.element_to_be_clickable((By.XPATH, '//*[@text="手动输入添加"]')))
		self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
		time.sleep(5)
		# 输入名字、手机号、设置部门，点击保存
		self.driver.find_element_by_xpath('//*[contains(@text,"姓名")]/../*[@class="android.widget.EditText"]').send_keys(name)
		self.driver.find_element_by_xpath('//*[contains(@text,"手机")]/..//*[@text="手机号"]').send_keys(telephone)
		self.driver.find_element_by_xpath('//*[@text="设置部门"]').click()
		self.driver.find_element_by_xpath('//*[@text="确定(1)"]').click()
		self.driver.find_element_by_xpath('//*[@text="保存"]').click()
		# #获取保存后的弹窗的文字
		text=self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
		assert  "添加成功"==text



