from time import sleep

from appium import webdriver


class TestAppiumWebdriver:
	def setup(self):
		desired_caps = {
        "platformName": "Android",
        "platformVersion":'6.0',
        "deviceName": "127.0.0.1:7555",
        "browserName": "Browser",
		#"chromedriverExecutable":"D:/DownloadTools/chromedriver_win32/chromedriver.exe",
		"chromedriverExecutableDir":"D:/DownloadTools/chromedriver_win32",
        "noReset":"true",
		"skipDeviceInitialization":"true"
        # "newCommandTimeout":60000
        }
		self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
		self.driver.implicitly_wait(30)

	def teardown(self):
		pass

	def test_browser(self):
		self.driver.get("http://m.baidu.com")
		sleep(5)
		self.driver.find_element_by_id("index-kw").click()
		sleep(3)
		self.driver.find_element_by_id("index-kw").send_keys("appium")
		self.driver.find_element_by_id("index-bn").click()
