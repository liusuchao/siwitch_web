# -*- coding:utf-8 -*-
import sqlalchemy
import pymysql
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from datetime import datetime  
from sqlalchemy.orm import sessionmaker,relation,relationship
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer  

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/liusuchao",encoding='utf-8',echo=True)
base=declarative_base()

class User(base):
	__tablename__ = 'user' 
	id = Column(Integer,primary_key=True,autoincrement=True)
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
			return data['id'] 
		except:
			return False

class UserBindDev(base):
	__tablename__ = 'user_bind_dev' 
	id = Column(Integer,primary_key=True,autoincrement=True)
	dev_id  = Column(String(64),unique=True)
	created = Column(DateTime(),default=datetime.now)
	updated = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
	dev_list = relationship("User", backref="llll")
	user_id = Column(Integer, ForeignKey("user.id"))
	def __repr__(self):
		return "<User('%s','%s','%s')>" % (self.dev_id, self.created, self.updated)

def init_db():
	base.metadata.create_all(engine)

def drop_db():
	base.metadata.drop_all(engine)

def add_user_db(user,password,email=''):
	session_class = sessionmaker(bind=engine)
	session = session_class()
	info=User()
	info.user = user
	info.password = password
	info.email = email
	k=info.generate_token()
	hh =info.verify_token(k)
	try:
		session.add(info)
		session.commit()
		return True
	except:
		return False
	finally:
		session.close()

def query_db_if_user(user):
	session_class = sessionmaker(bind=engine)
	session = session_class()
	try:
		my_user = session.query(User).filter_by(user=user).first()  # ≤È—Ø
		if my_user == None:
			my_user = False
		return my_user
	except:
		return False
	finally:
		session.close()

def add_dev_db(user,dev):
	session_class = sessionmaker(bind=engine)
	session = session_class()
	try:
		my_user = session.query(User).filter_by(user=user).first()
		my_dev=UserBindDev()
		my_dev.dev_id = dev
		my_dev.dev_list =my_user
		session.add(my_dev)
		session.add(my_user)
		session.commit()
		return True
	except:
		return False
	finally:
		session.close()

def get_dev_db(user):
	session_class = sessionmaker(bind=engine)
	session = session_class()
	try:
		my_user = session.query(User).filter_by(user=user).first()
		return my_user.llll
	except:
		return False
	finally:
		session.close()



