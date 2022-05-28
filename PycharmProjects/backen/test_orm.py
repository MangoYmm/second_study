from sqlalchemy import  create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = '192.168.5.130'
user = 'root'
password = '123456'
db = 'mysql'
charset = 'utf8mb4'

Base=declarative_base()

class User(Base):
	__tablename__='person'
	id=Column(Integer,primary_key=True)
	name=Column(String)
	age = Column(String)
	gender=Column(String)

def test_orm():
	engine=create_engine(
		'mysql+pymysql://{user}:{password}@{host}/{db}'.format(
			host=host,db=db,user=user,password=password),
			echo=True
	)
	Session=sessionmaker(bind=engine)
	session=Session()
	#数据插入
	u1=User(
		name='abc',
		age=20,
		gender='123@qq.com'
	)
	session.add(u1)
	session.commit()

	u2=session.query(User).filter_by(name='abc').first()
	print(u2.name)