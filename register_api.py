
#coding:utf-8
from zz_include import error_code
from flask_restful import reqparse, Resource
from json_object import JsonObject
import zz_email_database
import user
import tools
register=reqparse.RequestParser()

# class Register(Resource):
	# def get(self):
		# pass
	# def post(self):
		# register.add_argument('username',required=True,help="Username is Required")
		# register.add_argument('password',required=True,help="Password is Required")
		# args=register.parse_args()
		# username = args['username']
		# password = args['password']
		# jsobj = JsonObject()
		# jsobj.put("code",1)
		# jsobj.put("desc","User Existed")
		# jsobj.put("username",username)
		# jsobj.put("password",password)
		# return jsobj.getJson(),200
		
class Register(Resource):
	def get(self):
		pass
	def post(self):
		print("111111111111"*10)
		register.add_argument('username',required=True,help="Username is Required")
		register.add_argument('password',required=True,help="Password is Required")
		register.add_argument('verify',required=True,help="verify is Required")
		args=register.parse_args()
		username = args['username']
		password = args['password']
		verify = args['verify']
		jsobj = JsonObject()
		print("liusuchao@126.com"*10)
		jsobj.put("ret_code",error_code['succeed'])
		if False == zz_email_database.query_db1(username,verify):
			jsobj.put("ret_code",error_code['verify_not_exist'])
			print("111111111111")
			return jsobj.getJson(),200
		if False != user.query_db(username):
			jsobj.put("ret_code",error_code['user_exist'])
			return jsobj.getJson(),200
		if False == user.add_db(username,password,):
			jsobj.put("ret_code",error_code['unknown'])
			return jsobj.getJson(),200
		return jsobj.getJson(),200