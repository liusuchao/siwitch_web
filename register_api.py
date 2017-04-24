
#coding:utf-8
from zz_include import error_code
from flask_restful import reqparse, Resource
from json_object import JsonObject
import zz_verify_database
import zz_user_database
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
		register.add_argument('username',required=True,help="Username is Required")
		register.add_argument('password',required=True,help="Password is Required")
		register.add_argument('verify',required=True,help="verify is Required")
		args=register.parse_args()
		username = args['username']
		password = args['password']
		verify = args['verify']
		jsobj = JsonObject()
		jsobj.put("ret_code",error_code['succeed'])
		if False == zz_verify_database.query_db_if_valid(username,verify):
			jsobj.put("ret_code",error_code['verify_not_exist'])
		elif False != zz_user_database.query_db_if_user(username):
			jsobj.put("ret_code",error_code['user_exist'])
		elif False == zz_user_database.add_db(username,password,):
			jsobj.put("ret_code",error_code['unknown'])
		return jsobj.getJson(),200