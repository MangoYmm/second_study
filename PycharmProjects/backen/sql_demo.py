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

#每个列表示一张表，类中的每个变量表示一个表列
class UserTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120), nullable=True)

    #魔法方法，定义打印的格式
    def __repr__(self):
        return '<User %r>' % self.username
if __name__=='__main__':
    #新建表
    #db.create_all()
    #删除表
    #db.drop_all()
    #新增数据
    #实例化Usertest对象
    # row1=UserTest(id=1,username='安迪',email='123@qq.com',gender='女')
    # row2 = UserTest(id=2, username='张三', email='1234@qq.com',gender='男')
    # row3 = UserTest(id=3, username='李四', email='1235@qq.com',gender='男')
    # db.session.add(row1)
    # db.session.add_all([row2,row3])
    # # #对数据改变，都需要commit
    # db.session.commit()
    #查询数据
    #第一种写法
    resp=UserTest.query.filter_by(gender='男').first()
    #resp = UserTest.query.all()
    #print(resp.username,resp.gender)
    print(resp)
    # 第二种写法
    # resp = db.session.query(UserTest.id,UserTest.username,UserTest.gender).filter(UserTest.gender=='男').all()
    # print(resp)
    #print(resp[0][1],resp[1][1])
    #修改数据
    #第一种写法
    # resp=UserTest.query.filter_by(gender='男').first()
    # resp.gender="女"
    # db.session.commit()
    #第二种写法
    # UserTest.query.filter_by(gender='男').update({"username":"王四"})
    # db.session.commit()
    #删除数据
    UserTest.query.filter_by(gender='女').delete()
    db.session.commit()