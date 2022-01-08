import json
import configparser
from RecordedVideoPrac.InterfaceCI.library.httpclient import HttpClient


class Base:
	def __init__(self):
		config = configparser.ConfigParser()
		config.read("../config/config.ini", encoding="utf-8")
		config.sections()  # 获取section节点
		config.options('get_weather_info')  # 获取get_weather_info节点所有键
		self.host = config.get("get_weather_info", "host")  # 获取指定节点下的options的值
		self.ep_path = config.get("get_weather_info", "ep_path")
		self.client=HttpClient()

	def get_cityname(self,number):
		url = self.host + self.ep_path + f'{number}.html'
		response = self.client.get(url)
		city = json.loads(response).get('weatherinfo').get('city')
		return  city