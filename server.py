#coding:utf-8
from flask import Flask
from flask_restful import Api
from auth_api import *

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
	return 'Hello,World'

api.add_resource(Authentication,'/auth')

if __name__ == '__main__':
	app.run("192.168.1.119")