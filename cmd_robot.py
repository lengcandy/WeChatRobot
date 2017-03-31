#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
#设置robot信息
KEY = "5fa3c2dcf5254677a0de9e370fcf781e"
user_id = "nanimo"

#获取robot回复
def get_response(msg):
	api_url = "http://www.tuling123.com/openapi/api"
	
	data = {
			'key' : KEY,
			'info' : msg,
			'userif' : user_id
			}
	try:
		#发送指令
		r = requests.post(api_url,data=data).json()
		return r.get('text')
	except:
		return
	
if __name__ == "__main__":
	print "input 0 to stop.\n"
	while True:
		msg = raw_input('You : ').decode("gbk")
		#用户输入0停止运行
		if msg=='0':
			break
		recieve = get_response(msg)
		print 'robot : ' + recieve