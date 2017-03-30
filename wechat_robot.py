#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import itchat

KEY = "5fa3c2dcf5254677a0de9e370fcf781e"
user_id = "weekdawn"

def get_response(msg):
	api_url = "http://www.tuling123.com/openapi/api"
	
	data = {
			'key' : KEY,
			'info' : msg,
			'userif' : user_id
			}
	try:
		r = requests.post(api_url,data=data).json()
		print "requests successfully"
		return r.get('text')
	except:
		return

@itchat.msg_register(itchat.content.TEXT)
def text_relpy(msg):
	reply = get_response(msg['Text'])
	
	return reply
		
itchat.auto_login(hotReload=True)
itchat.run()
# wechat_id = 'z925439649'
# itchat.send('hello i am test',toUserName=wechat_id)	
# itchat.logout()