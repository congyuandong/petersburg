#coding:utf-8
from django.db import models

# Create your models here.

'''
客户表 发布方
'''
class client(models.Model):
	clt_mail = models.EmailField(verbose_name='Email')
	clt_pwd = models.CharField(max_length=20,verbose_name='密码')
	clt_name = models.CharField(max_length=50,verbose_name='用户名')
	clt_tel = models.CharField(max_length=30,verbose_name='联系电话')
	clt_company = models.CharField(max_length=50,verbose_name='公司名称')
	clt_position = models.CharField(max_length=30,verbose_name='职位')
	clt_industry = models.CharField(max_length=30,verbose_name='行业')
	clt_from = models.CharField(max_length=30,verbose_name='获知本网站途径')

	def __unicode__(self):
		return self.ctl_name

	class Meta:
		verbose_name = '发货企业'
		verbose_name_plural = '发货企业'


'''
司机 driver
'''
class driver(models.Model):
	dr_name = models.CharField(max_length=50,verbose_name='姓名')
	dr_iden =  models.CharField(max_length=50,verbose_name='身份证号码')
	dr_tel = models.CharField(max_length=30,verbose_name='手机号码')
	dr_number = models.CharField(max_length=50,verbose_name='车牌号码')
	dr_hand = models.CharField(max_length=50,verbose_name='挂车号码')
	dr_type = models.CharField(max_length=50,verbose_name='车辆类型')
	dr_length = models.CharField(max_length=50,verbose_name='车辆长度')
	dr_weight = models.CharField(max_length=50,verbose_name='最大载重')
	dr_pwd = models.CharField(max_length=20,verbose_name='密码')

	def __unicode__(self):
		return self.dr_name

	class Meta:
		verbose_name = '货车司机'
		verbose_name_plural = '货车司机'