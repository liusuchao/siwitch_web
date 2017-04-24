# -*- coding:utf-8 -*-
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

class Dev(base):
	__tablename__ = 'dev' 
	id = Column(Integer,primary_key=True,autoincrement=True)
	uid = Column(String(32),unique=True)
	created = Column(DateTime(),default=datetime.now)
	updated = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
	def __repr__(self):
		return "<User('%s','%s', '%s', '%s', '%s')>" % (self.user, self.password, self.email, self.created, self.updated)

def init_db():
	base.metadata.create_all(engine)

def drop_db():
	base.metadata.drop_all(engine)