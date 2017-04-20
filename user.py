import sqlalchemy
import pymysql

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from datetime import datetime  
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@192.168.9.119/liusuchao",encoding='utf-8',echo=True)
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

def init_db():
    base.metadata.create_all(engine)

def drop_db():
    base.metadata.drop_all(engine)
	
def add_db(user,password,email):
	session_class = sessionmaker(bind=engine)
	session = session_class()
	test=User(user="gfdgsd",password="fdsfasf",email="gfdsgdfg")
	session.add(test)
	session.commit()

def query_db():
	my_user = session.query(User).filter_by(email="liusuchao@126.com").all()  # 查询

	
	
	
# def to_dict(self):
    # return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

# def row2dict(row):
    # d = {}
    # for column in row.__table__.columns:
        # d[column.name] = str(getattr(row, column.name))
    # return d
	

