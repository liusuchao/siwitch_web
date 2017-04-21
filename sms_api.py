
#coding:utf-8
import sms
import sms_verify
import tools
from flask_restful import reqparse, Resource
from json_object import JsonObject

temp=reqparse.RequestParser()

class GetSmsCode(Resource):
	def get(self):
		pass
	def post(self):
		temp.add_argument('username',required=True,help="Username is Required")
		args=temp.parse_args()
		username = args['username']
		jsobj = JsonObject()
		jsobj.put("code",False)
		sms_dict = sms_verify.send_verification_code(username)
		if sms_dict['code'] == 200:
			if False != sms.add_db(username,sms_dict['obj']):
				jsobj.put("code",True)
				jsobj.put("verify",sms_dict['obj'])
		jsobj.put("username",username)
		return jsobj.getJson(),200