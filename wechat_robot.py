#coding=utf-8
#Name : wechat_robot.py
#Version : 1.0
#function : just a wechat_robot
#Author : weekdawn

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import itchat
#设置机器人信息
KEY = "5fa3c2dcf5254677a0de9e370fcf781e"
user_id = "weekdawn"
#获取图灵机器人自动回复信息
def get_response(msg):
	#信息传送网址
	api_url = "http://www.tuling123.com/openapi/api"

	data = {
			'key' : KEY,
			'info' : msg,
			'userif' : user_id
			}
	try:
		#向图灵机器人发送请求
		r = requests.post(api_url,data=data).json()
		print "requests successfully"
		#返回自动回复信息
		return r.get('text')
	except:
		return
#设置微信的接收文字自动回复
@itchat.msg_register(itchat.content.TEXT)
def text_relpy(msg):
	#传入接收到的文字信息
	reply = get_response(msg['Text'])
	#返回图灵机器人回复信息
	return reply
#保持登录状态，下次登录可不用扫描二维码
itchat.auto_login(hotReload=True)
itchat.run()
