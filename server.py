#coding:utf-8
from flask import Flask
from flask_restful import Api
from auth_api import *
from register_api import *
from sms_api import *

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
	return 'Hello,World'

api.add_resource(Authentication,'/auth')
api.add_resource(Register,'/register')
api.add_resource(GetSmsCode,'/sms')

if __name__ == '__main__':
	app.run("192.168.9.119")
