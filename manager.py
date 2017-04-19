#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Leon xie
import user
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
def init_db():
	user.init()
	
@manager.command
def add_db():
	user.add()
	
if __name__ == '__main__':
    manager.run()