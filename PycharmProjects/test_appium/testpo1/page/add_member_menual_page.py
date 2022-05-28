from test_appium.testpo1.page.base import Base
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.testpo1.page.edit_member_page import EditMemberPage


class AddMemberMenualPage(Base):
	_WINDOW_TEXT=(By.XPATH,'//*[@class="android.widget.Toast"]')
	_MENUALINPUT_BUTTON=(By.XPATH,'//*[@text="手动输入添加"]')
	def click_add_member_menual(self):
		# 点击手动输入添加
		WebDriverWait(self.driver, 30).until(
			expected_conditions.element_to_be_clickable(self._MENUALINPUT_BUTTON))
		#self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
		self.find_and_click(*self._MENUALINPUT_BUTTON)
		time.sleep(5)
		return  EditMemberPage(self.driver)
	def get_after_add_member_text(self):
		# #获取保存后的弹窗的文字
		#text = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
		return  self.get_text(*self._WINDOW_TEXT)