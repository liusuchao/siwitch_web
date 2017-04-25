#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Leon xie
import zz_user_database 
import tools
from flask_script import Manager
from app import app


manager = Manager(app)

@manager.command
def hello():
	print("hello world")

@manager.option('-m','--msg',dest='msg_val',default='world')
def hello_world(msg_val):
	print('hello'+msg_val)

@manager.command
def init():
	zz_user_database.init_db()

@manager.command
def drop():
	zz_user_database.drop_db()

	
@manager.command
def add_user():
	zz_user_database.add_user_db("liusuchao","12345678")
	#pass

@manager.command
def add_dev():
	zz_user_database.add_dev_db("liusuchao","009")
	zz_user_database.add_dev_db("liusuchao","010")
	# pass

@manager.command
def get_dev():
	print(zz_user_database.get_dev_db("liusuchao"))
	# pass

@manager.command
def query():
	pass

if __name__ == '__main__':
    manager.run()