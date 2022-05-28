import  requests

from log_util import logger


class TestCase:
	"""
	增删改查
	"""
	def setup_class(self):
		self.url='http://127.0.0.1:5001/hogwarts'

	def test_select(self):
		"""
		查询用例
		:return:
		"""

		resp = requests.get(self.url)
		logger.info(resp.json())
		assert  resp.status_code==200

		param={"id":1}
		resp1 = requests.get(self.url,params=param)
		logger.info(resp1.json())
		assert resp1.status_code == 200


	def test_add(self):
		"""
		新增用例
		:return:
		"""
		# data = {
		# 	"id": 1,
		# 	"node_id": "node_id1",
		# 	"remark": "新增的第一条用例"
		# }
		data = {
			"id": 3,
			"node_id": ['node_id3','node_id4'],
			"remark": "新增的第3条用例"
		}
		resp = requests.post(self.url,json=data)
		logger.info(resp.json())
		assert  resp.status_code==200

	def test_delete(self):
		"""
		删除用例
		:return:
		"""
		param={"id":11}
		resp = requests.delete(self.url,params=param)
		logger.info(resp.json())
		assert  resp.status_code==200

	def test_update(self):
		"""
		修改用例
		:return:
		"""
		data={"id": 3,
			"node_id": ['node_id3','node_id4'],
			"remark": "修改的第3条用例的remark"}
		resp = requests.put(self.url,json=data)
		logger.info(resp.json())
		assert  resp.status_code==200


# def test_post():
# 	resp=requests.post('http://127.0.0.1:5001/hogwarts',json={"teacher":"ad"})
# 	print(resp.text)