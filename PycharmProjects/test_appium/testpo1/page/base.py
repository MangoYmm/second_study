import logging

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Base:
	def __init__(self,driver=None):
		self.driver=driver

	def log_info(self,message):
		logging.info(message)

	def find_ele(self,By,locate):
		self.log_info("find")
		ele=self.driver.find_element(By,locate)
		return  ele

	def find_and_click(self,By,locate):
		self.log_info("find_and_click")
		self.find_ele(By,locate).click()

	def find_and_sendkeys(self,By,locate,text):
		self.find_ele(By,locate).send_keys(text)

	def get_text(self,By,locate):
		text=self.find_ele(By,locate).text
		return text

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
				#print(wind)
				height=wind["height"]
				width = wind["width"]
				start_x = width*0.6
				start_y = height*0.8
				end_x=start_x
				end_y=height*0.3
				self.driver.swipe(start_x,start_y,end_x,end_y,2000)
				self.driver.implicitly_wait(5)
			if i ==num-1:
				raise NoSuchElementException(f"找了{i}次,都没找到")
	def back(self,num=3):
		for i in range(num):
			self.driver.back()