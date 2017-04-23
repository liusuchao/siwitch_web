#coding:utf-8
from flask import Flask
from flask_restful import Api
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)
api = Api(app)

from zz_email_api import GetEmailCode
from auth_api import Authentication
from register_api import Register
from sms_api import GetSmsCode

@app.route('/')
def hello_world():
	return 'Hello,World'


api.add_resource(Authentication,'/auth')
api.add_resource(Register,'/register')
api.add_resource(GetSmsCode,'/sms')
api.add_resource(GetEmailCode,'/get_email_code')

if __name__ == '__main__':
	app.run(host= "192.168.16.119",port=8000)

