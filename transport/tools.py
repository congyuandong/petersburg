#coding:utf-8
from django.core.mail import send_mail

FullPath = 'http://192.168.2.114:8080/t/conf_mail'

def SendMailConfirm(mail_address):
	mail_address = str(mail_address)
	print '已经向'+mail_address+'发送确认邮件'
	send_mail('至诚迅达邮箱确认','请点击以下连接进行确认\n'+FullPath+'?mail='+mail_address,'zhichengxunda@163.com',[mail_address],fail_silently=True)

