from selenium.webdriver.common.by import By

from test_appium.testpo1.page.base import Base


class EditMemberPage(Base):
	_NAME_BOX=(By.XPATH,'//*[contains(@text,"姓名")]/../*[@class="android.widget.EditText"]')
	_TELEPHONE_BOX=(By.XPATH,'//*[contains(@text,"手机")]/..//*[@text="手机号"]')
	_SET_DEPARTMENT=(By.XPATH,'//*[@text="设置部门"]')
	_SUBMIT=(By.XPATH,'//*[@text="确定(1)"]')
	_SAVE=(By.XPATH,'//*[@text="保存"]')
	def add_member_info(self,name,telephone):
		from test_appium.testpo1.page.add_member_menual_page import AddMemberMenualPage
		# 输入名字、手机号、设置部门，点击保存
		# self.driver.find_element_by_xpath('//*[contains(@text,"姓名")]/../*[@class="android.widget.EditText"]').send_keys(
		# 	name)
		# self.driver.find_element_by_xpath('//*[contains(@text,"手机")]/..//*[@text="手机号"]').send_keys(telephone)
		# self.driver.find_element_by_xpath('//*[@text="设置部门"]').click()
		# self.driver.find_element_by_xpath('//*[@text="确定(1)"]').click()
		# self.driver.find_element_by_xpath('//*[@text="保存"]').click()
		self.find_and_sendkeys(*self._NAME_BOX,name)
		self.find_and_sendkeys(*self._TELEPHONE_BOX,telephone)
		self.find_and_click(*self._SET_DEPARTMENT)
		self.find_and_click(*self._SUBMIT)
		self.find_and_click(*self._SAVE)
		return  AddMemberMenualPage(self.driver)