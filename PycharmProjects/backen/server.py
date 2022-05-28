import json
import os,sys
#print(sys.path)
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from log_util import logger
from flask_restful import  Resource,Api
#实例化flask,获得实例对象app
app = Flask(__name__)
#绑定app实例至Api
api=Api(app)

host = '192.168.5.130'
port=3306
user = 'root'
password = '123456'
db = 'mysql'
charset = 'utf8mb4'
#连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(
			host=host,db=db,user=user,password=password,port=port)
#sqlite:////tmp/test.db这是一个本地的数据库，前三个/是固定格式
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#SQLAlchemy绑定app
db = SQLAlchemy(app)
#每个列表示一张表，类中的每个变量表示一个表列
class TestCase(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	node_id = db.Column(db.String(80), nullable=False)
	remark = db.Column(db.String(120), nullable=False)
	def  as_dict(self):
		return {
			"id":self.id,
			"node_id":self.node_id,
			"remark":self.remark}

# @app.route("/hogwarts",methods=['get'])
# def select_case():
# 	#日志打印
# 	#app.logger.info("we receive a get")
# 	logger.info("get method")
# 	#接口的响应值，对应的就是return的内容
# 	return {"code":0,"msg":"get success"}
#
# @app.route("/hogwarts",methods=['post'])
# def add_case():
# 	logger.info("post method")
# 	#接口的响应值，对应的就是return的内容
# 	return {"code":0,"msg":"post success"}
#
# @app.route("/hogwarts",methods=['put'])
# def update_case():
# 	logger.info("put method")
# 	#接口的响应值，对应的就是return的内容
# 	return {"code":0,"msg":"put success"}
#
# @app.route("/hogwarts",methods=['delete'])
# def delete_case():
# 	logger.info("delete method")
# 	#接口的响应值，对应的就是return的内容
# 	return {"code":0,"msg":"delete success"}
class TestServer(Resource):
	def get(self):
		"""
		测试用例的查询
		:return:
		"""
		case_id=request.args.get("id")
		if case_id:
			case_data=TestCase.query.filter_by(id=case_id).first()
			if case_data:
				#datas=[{"id":case_data.id,"node_id":case_data.node_id,"remark":case_data.remark}]
				datas=[case_data.as_dict()]
				logger.info(f"为{case_id}的id存在，对应的结果为：{datas}")

			else:
				datas=[]
				logger.info(f"为{case_id}的id 不存在")

		else:
			case_datas = TestCase.query.all()
			#datas=[{"id":case_data.id,"node_id":case_data.node_id,"remark":case_data.remark} for case_data in case_datas]
			datas=[case_data.as_dict() for case_data in case_datas]
			logger.info(f"没有传ID，返回所有的结果")
		#接口的响应值，对应的就是return的内容
		return {"code":0,"msg":{"datas":datas}}

	def post(self):
		"""
		测试用例的新增
		:return:
		"""
		#获取测试接口中传入的json数据
		case_data=request.json
		logger.info(f"{case_data}")
		case_id=case_data.get("id")
		if not TestCase.query.filter_by(id=case_id).first():
			testcase=TestCase(**case_data)
			#json.dumps()将python对象转成json字符串
			testcase.node_id= json.dumps(case_data.get("node_id"))
			db.session.add(testcase)
			db.session.commit()
			logger.info("新增成功")
			#接口的响应值，对应的就是return的内容
			return {"code":0,"msg":f"Case id {case_id} added successful"}
		else:
			logger.info("新增失败")
			return {"code": 40001, "msg": f"Case id {case_id} is exist"}

	def put(self):
		"""
		测试用例的更新
		:return:
		"""
		testcase=request.json
		print(testcase)
		case_id=testcase.get("id")
		testcase["node_id"]=json.dumps(testcase.get("node_id"))
		if not TestCase.query.filter_by(id=case_id).first():
			logger.info(f"id:{case_id}不存在")
			return {"code": 40001, "msg": f"id:{case_id}不存在"}
		else:
			TestCase.query.filter_by(id=case_id).update(testcase)
			db.session.commit()
			logger.info("修改成功")
			#接口的响应值，对应的就是return的内容
			return {"code":0,"msg":"put success"}

	def delete(self):
		"""
		测试用例的删除
		:return:
		"""
		case_id = request.args.get("id")
		if not case_id:
			logger.info(f"{case_id}不能为空")
			return {"code": 40002, "msg": "id:{case_id}不能为空"}
		if not TestCase.query.filter_by(id=case_id).first():
			logger.info(f"id:{case_id}不存在")
			return {"code": 40001, "msg": "id:{case_id}不存在"}
		else:
			TestCase.query.filter_by(id=case_id).delete()
			db.session.commit()
			logger.info("删除成功")
			#接口的响应值，对应的就是return的内容
			return {"code":0,"msg":"删除为{case_id}的id success"}
#给实例指定资源
api.add_resource(TestServer,'/hogwarts')

if __name__=='__main__':
	#db.create_all()
	app.run(debug=True,port=5001)