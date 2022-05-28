from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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

class  UserInfo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	age = db.Column(db.Integer)
	ut = db.relationship('UserType')

class  UserType(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	user_info_id = db.Column(db.Integer,db.ForeignKey("user_info.id"))

if __name__=='__main__':
	#db.create_all()
	#db.drop_all()
	# UIrow1 = UserInfo(name="安迪", age=18)
	# UIrow2 = UserInfo(name="张三", age=19)
	# UIrow3 = UserInfo(name="李四", age=20)
	# UIrow4 = UserInfo(name="王五", age=21)
	# UIrow5 = UserInfo(name="老六", age=22)
	# UIrow6 = UserInfo(name="老七", age=23)
	#UIrow18 = UserInfo(name="老八", age=23)
	#db.session.add_all([UIrow1,UIrow2,UIrow3,UIrow4,UIrow5,UIrow6])
	# db.session.add_all([UIrow18])
	#flush() 会将session中的数据刷到数据库中，使数据库主键自增；但不会写到磁盘里
	# db.session.flush()
	# UTrow1 = UserType(title="管理用户", user_info_id=UIrow1.id)
	# UTrow2 = UserType(title="高级用户", user_info_id=UIrow1.id)
	# UTrow3 = UserType(title="普通用户", user_info_id=UIrow1.id)
	# UTrow4 = UserType(title="管理用户", user_info_id=UIrow2.id)
	# UTrow5 = UserType(title="高级用户", user_info_id=UIrow3.id)
	# UTrow6 = UserType(title="普通用户", user_info_id=UIrow4.id)
	# UTrow7 = UserType(title="高级用户", user_info_id=UIrow5.id)
	# UTrow8 = UserType(title="普通用户", user_info_id=UIrow6.id)
	#UTrow16 = UserType(title="普通用户", user_info_id=UIrow18.id)
	#db.session.add_all([UTrow1, UTrow2, UTrow3, UTrow4, UTrow5, UTrow6, UTrow7, UTrow8])
	# db.session.add_all([UTrow16])
	# db.session.commit()
	#多表关联查询
	resp = db.session.query(UserInfo.id, UserInfo.name, UserType.title).\
		join(UserInfo,UserType.user_info_id==UserInfo.id).filter(UserInfo.name == "王五").all()
	print(resp)
