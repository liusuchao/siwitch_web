#coding:utf-8
from flask_restful import reqparse, Resource
from json_object import JsonObject
from zz_email_database import query_db,add_db
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
		code = generate_verification_code(4)
		jsobj = JsonObject()
		jsobj.put("ret_code",1)
		print(type(username))
		print(type(code))
		while False != query_db(code):
			code = generate_verification_code(4)
		if True == add_db(username,code):
			send_verify(username,code)
			jsobj.put("ret_code",0)
		# sms_dict = sms_verify.send_verification_code(username)
		# if sms_dict['code'] == 200:
			# if False != sms.add_db(username,sms_dict['obj']):
				# jsobj.put("code",True)
				# jsobj.put("verify",code)
		return jsobj.getJson(),200