
#coding:utf-8

from flask_restful import reqparse, Resource
from json_object import JsonObject
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
		register.add_argument('username',required=True,help="Username is Required")
		register.add_argument('password',required=True,help="Password is Required")
		args=register.parse_args()
		username = args['username']
		password = args['password']
		jsobj = JsonObject()
		jsobj.put("code",False)
		if False != user.query_db(username):
			if False != user.add_db(username,password,):
				jsobj.put("code",True)
		jsobj.put("username",username)
		jsobj.put("password",password)
		return jsobj.getJson(),200