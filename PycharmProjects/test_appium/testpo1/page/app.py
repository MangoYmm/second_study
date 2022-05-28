from appium import webdriver

from test_appium.testpo1.page.base import Base
from test_appium.testpo1.page.main_page import MainPage


class App(Base):
	def start(self):
		if self.driver==None:
			desired_caps = {
				"platformName": "Android",
				"platformVersion": "6.0",
				# "deviceName": "192.168.18.101:5555",
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

		else:
			print("有diver，复用driver")
			#launch_app()会启动caps中指定的应用，剩去与server建立链接的过程
			self.driver.launch_app()
		return self
			#start_activity()可以启动任何应用，即参数中指定的appPackage、appActivity
			#self.driver.start_activity('appPackage','appActivity')

	def restart(self):
		self.driver.close()
		self.driver.launch_app()

	def quit(self):
		self.driver.quit()

	def goto_main(self):
		#进入主页 入口
		return MainPage(self.driver)