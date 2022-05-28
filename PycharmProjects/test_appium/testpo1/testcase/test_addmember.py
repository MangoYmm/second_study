import time

import pytest
from faker import Faker

from test_appium.testpo1.page.app import App


class TestContact:
	def setup_class(self):
		self.fake = Faker('zh_CN')
		self.app = App()
	def setup(self):
		self.main=self.app.start().goto_main()

	def teardown(self):
		#self.app.restart()
		self.app.back(5)

	def teardown_class(self):
		self.app.quit()

	def test_add_member(self):
		name = self.fake.name()
		telephone = self.fake.phone_number()
		assert "添加成功"==self.main.goto_contactlist().goto_add_member_menual().click_add_member_menual().\
			add_member_info(name,telephone).get_after_add_member_text()

	def test_add_member1(self):
		name = self.fake.name()
		telephone = self.fake.phone_number()
		time.sleep(5)
		assert "添加成功"==self.main.goto_contactlist().goto_add_member_menual().click_add_member_menual().\
			add_member_info(name,telephone).get_after_add_member_text()