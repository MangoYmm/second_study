from selenium.webdriver.common.by import By

from test_appium.testpo1.page.base import Base
from test_appium.testpo1.page.contact_list_page import ContactList


class MainPage(Base):
	_CONTACT_BUTTON=(By.XPATH,"//*[@text='通讯录']")
	def goto_contactlist(self):
		# 点击通讯录
		#self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
		self.find_and_click(*self._CONTACT_BUTTON)
		return ContactList(self.driver)