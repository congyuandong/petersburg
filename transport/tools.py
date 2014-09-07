#coding:utf-8
import random
import string
from django.core.mail import send_mail

FullPath = 'http://localhost:8080/t/conf_mail'

#发送邮箱确认邮件
def SendMailConfirm(mail_address):
	mail_address = str(mail_address)
	print '已经向'+mail_address+'发送确认邮件'
	send_mail('至诚迅达邮箱确认','请点击以下连接进行确认\n'+FullPath+'?mail='+mail_address,'zhichengxunda@163.com',[mail_address],fail_silently=True)


#发送找回密码验证码
def SendMailCode(code,mail_address):
	code = str(code)
	mail_address = str(mail_address)
	print '已经向'+mail_address+'发送确认邮件'
	send_mail('至诚迅达密码修改','请在密码修改页面输入以下验证码:'+code,'zhichengxunda@163.com',[mail_address],fail_silently=True)

#随机产生六个字符
def RandCode():
	return string.join(random.sample(['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A','1','2','3','4','5','6','7','8','9','0'], 6)).replace(' ','')

