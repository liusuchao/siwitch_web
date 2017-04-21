import sqlalchemy
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/liusuchao",encoding='utf-8',echo=True)
base=declarative_base()

class Verify(base):
	__tablename__ = 'verify' 
	user = Column(String(32),primary_key=True)
	verify = Column(String(64))
	update = Column(DateTime(),default=datetime.now)
	def __repr__(self):
		return "<User('%s','%s', '%s')>" % (self.user, self.verify, self.update)

def init_db():
    base.metadata.create_all(engine)

def drop_db():
    base.metadata.drop_all(engine)
	
def add_db(user,verify):
	session_class = sessionmaker(bind=engine)
	session = session_class()
	try:
		info=Verify()
		info.user = user
		info.verify = verify
		info.update = datetime.now()
		session.merge(info)
		session.commit()
		return True
	except:
		return False
	finally:
		session.close()

def query_db(user,verify):
	now = datetime.now()
	now_str=now.strftime("%Y-%m-%d %H:%M:%S")
	toDate = datetime.strptime(now_str, "%Y-%m-%d %H:%M:%S")  -  timedelta(minutes=3)
	print("------")
	print(toDate)
	print(type(toDate))
	print("------")
	session_class = sessionmaker(bind=engine)
	session = session_class()
	try:
		my_user = session.query(Verify).filter(Verify.user  == user,Verify.verify  == verify,Verify.update  >= toDate).first()  # ≤È—Ø
		session.delete(my_user)
		session.commit()
		return True
	except:
		return False
	finally:
		session.close()
	
	
	


