import sqlalchemy
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from datetime import datetime  
from sqlalchemy.orm import sessionmaker

base=declarative_base() #生成ORM基类
class user(base):
	__tablename__ = 'user' #表名
	id = Column(Integer,primary_key=True) #字段，整形，主键 column是导入的
	user = Column(String(32))
	password = Column(String(64))
	email = Column(String(64),nullable=False)	
	created = Column(DateTime(),default=datetime.now)
	updated = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
	
def init():
	engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/liusuchao",encoding='utf-8',echo=True)
	base.metadata.create_all(engine)

def add():
	engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/liusuchao",encoding='utf-8',echo=True)
	Session_class = sessionmaker(bind=engine)
	Session = Session_class()
	test=user(user="liusuchao",password="123456789",email="liusuchao@126.com")
	Session.add(test)
	Session.commit()
