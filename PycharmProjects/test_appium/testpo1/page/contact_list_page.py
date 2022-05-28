from selenium.webdriver.common.by import By

from test_appium.testpo1.page.add_member_menual_page import AddMemberMenualPage
from test_appium.testpo1.page.base import Base


class ContactList(Base):
	_ADD_MEMBER_BUTTON_NAME="添加成员"
	def  goto_add_member_menual(self):
		# 点击添加成员
		# self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
		self.swipe_find(self._ADD_MEMBER_BUTTON_NAME, 8).click()
		return AddMemberMenualPage(self.driver)