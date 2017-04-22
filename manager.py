#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Leon xie
import user 
import tools
from flask_script import Manager
from server import app


manager = Manager(app)

@manager.command
def hello():
	print("hello world")
	
@manager.option('-m','--msg',dest='msg_val',default='world')
def hello_world(msg_val):
	print('hello'+msg_val)


@manager.command
def init():
	user.init_db()


	
@manager.command
def drop():
	user.drop_db()

	
@manager.command
def add():
	ret = user.add_db("lissusuchao","123")
	print('*'*10)
	print(ret)
	print('-'*10)

@manager.command
def query():
	ret = user.query_db("liusuchao",'123')
	print('*'*10)
	print(ret)
	print('-'*10)
	
if __name__ == '__main__':
    manager.run()