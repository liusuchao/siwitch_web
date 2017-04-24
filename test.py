# -*- coding:utf-8 -*-
import pymysql
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from datetime import datetime  
from sqlalchemy.orm import sessionmaker,relationship
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer  

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/liusuchao",encoding='utf-8',echo=True)
base=declarative_base()

class AddUser(base):
	__tablename__ = "add_user"
	user_id = Column(Integer,primary_key=True,autoincrement=True)
	user_name = Column(String(100))
	user_password = Column(String(100))
	user_sex = Column(String(50))
	user_province = Column(String(100))

class Hobby(base):
	__tablename__ = 'AddUser'
	hobby_id = Column(Integer,primary_key=True,autoincrement=True)
	hobby_name = Column(String(100))
	user_id = Column(Integer,ForeignKey("add_user.user_id"))
	user = relationship("AddUser",backref="hobbys")


base.metadata.create_all(engine)


search_user = AddUser(user_name="liusuchao", user_password="123", user_sex="sex", user_province="fsdafsf")
hobby = Hobby(hobby_name="xxxx")
hobby.user = search_user
hobby1 = Hobby(hobby_name="123123")
hobby1.user = search_user
session_class = sessionmaker(bind=engine)
session = session_class()
session.add(hobby1)
session.add(hobby1)
session.commit()