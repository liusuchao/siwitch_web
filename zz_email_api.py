#coding:utf-8
from zz_include import error_code
from flask_restful import reqparse, Resource
from json_object import JsonObject
from zz_verify_database import query_db_if_exist ,query_db_if_valid,add_db
from zz_user_database import query_db_if_user
from zz_verification_code import generate_verification_code
from zz_email import send_verify
temp=reqparse.RequestParser()

class GetEmailCode(Resource):
	def get(self):
		pass
	def post(self):
		temp.add_argument('username',required=True,help="Username is Required")
		args=temp.parse_args()
		username = args['username']
		jsobj = JsonObject()
		jsobj.put("ret_code",error_code['succeed'])

		code = generate_verification_code(4)
		while False != query_db_if_exist(code):
			code = generate_verification_code(4)
		if False != query_db_if_user(username):
			jsobj.put("ret_code",error_code['user_exist'])
		elif False == add_db(username,code):
			jsobj.put("ret_code",error_code['user_exist'])
		else:
			send_verify(username,code)
		return jsobj.getJson(),200