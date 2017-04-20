#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Leon xie
import user
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
	user.add_db("liusuchao","123","liusuchao@126.com")
	
@manager.command
def query():
	user.query_db()
	
if __name__ == '__main__':
    manager.run()