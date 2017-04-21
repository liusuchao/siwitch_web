import http.client
import urllib
import json
import time
import random
import string
import hashlib

APP_KYE = "3642d404c0cf06d8d0a1f07e2cc2a22d"
APP_SECRET = "76818144472e"
HEADERS = {"AppKey": " ", "CheckSum": " ","CurTime": " ", "Nonce": " ","Content-Type": ""}
PHONE = "mobile="

def post_data(head,info):
    try:
        data = dict()
        conn = http.client.HTTPSConnection("api.netease.im")
        conn.request("POST", "/sms/sendcode.action", info, head)
        response = conn.getresponse()
        b = response.read()
        # print(b)
        # print(response)
        # print(response.status)
        # print(response.reason)
        data = json.loads(b.decode())
    except Exception as err:
        print("error")
        print(err)
    conn.close()
    return data

def head_pack():
    hash = hashlib.sha1()
    cur_time = str(int(time.time()))
    nonce = ''.join(random.sample(string.ascii_letters + string.digits,32))
    temp_str = APP_SECRET + nonce+ cur_time
    hash.update(temp_str.encode('utf-8'))
    check_sum = hash.hexdigest()
    HEADERS["AppKey"] = APP_KYE
    HEADERS["CheckSum"] = check_sum
    HEADERS["CurTime"] = cur_time
    HEADERS["Nonce"] = nonce
    HEADERS["Content-Type"] = "application/x-www-form-urlencoded"
    return  HEADERS
#{'code': 200, 'msg': '101', 'obj': '2437'} ok
#{'code': 414, 'msg': "mobile '123132132' bad format!"}
def send_verification_code(phone_code):
    msg=post_data(head_pack(),PHONE+phone_code)
    return msg	
