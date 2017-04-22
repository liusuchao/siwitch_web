import sqlalchemy
import pymysql
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from datetime import datetime  
from sqlalchemy.orm import sessionmaker
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer  

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/liusuchao",encoding='utf-8',echo=True)
base=declarative_base()

class User(base):
	__tablename__ = 'user' #表名
	id = Column(Integer,primary_key=True,autoincrement=True) #字段，整形，主键 column是导入的
	user = Column(String(32),unique=True)
	password = Column(String(64))
	email = Column(String(64))	
	created = Column(DateTime(),default=datetime.now)
	updated = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
	def __repr__(self):
		return "<User('%s','%s', '%s', '%s', '%s')>" % (self.user, self.password, self.email, self.created, self.updated)
	def generate_token(self,expiration=15):   
		s=Serializer('secret key',expiration)   
		return s.dumps({'id':self.user}) 
	def verify_token(self,token):   
		s=Serializer('secret key')   
		try:
			data = s.loads(token)
			return data
		except:
			return False
		

		

def init_db():
    base.metadata.create_all(engine)

def drop_db():
    base.metadata.drop_all(engine)
	
def add_db(user,password,email=''):
	session_class = sessionmaker(bind=engine)
	session = session_class()
	info=User()
	info.user = user
	info.password = password
	info.email = email
	k=info.generate_token()

	time.sleep(10)
	hh =info.verify_token(k)
	print("**************")
	print(hh)
	print("----------")
	print(k)
	print("----------")
	try:

		print("----------")

		session.add(info)
		session.commit()
		return True
	except:
		return False
	finally:
		session.close()
	
def query_db(user):
	session_class = sessionmaker(bind=engine)
	session = session_class()
	try:
		my_user = session.query(User).filter_by(user=user).first()  # 查询
		return my_user
	except:
		return False
	finally:
		session.close()
	
	
	


