
#coding:utf-8
import user
import tools
from flask_restful import reqparse, Resource
from json_object import JsonObject

auth=reqparse.RequestParser()

class Authentication(Resource):
	def get(self):
		pass
	def post(self):
		auth.add_argument('username',required=True,help="Username is Required")
		auth.add_argument('password',required=True,help="Password is Required")
		args=auth.parse_args()
		username = args['username']
		password = args['password']
		jsobj = JsonObject()
		jsobj.put("code",1)
		jsobj.put("desc","User Existed")
		jsobj.put("username",username)
		jsobj.put("password",password)
		return jsobj.getJson(),200