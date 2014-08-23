#coding:utf-8
from django.db import models
import simplejson as json
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

	def toJSON(self):
		return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

	def __unicode__(self):
		return self.dr_name

	class Meta:
		verbose_name = '货车司机'
		verbose_name_plural = '货车司机'

'''
订单
'''
class order(models.Model):
	or_id = models.CharField(max_length=50,verbose_name='订单编号')
	or_start = models.CharField(max_length=500,verbose_name='装车地点')
	or_end = models.CharField(max_length=500,verbose_name='卸车地点')
	or_startTime = models.DateTimeField(verbose_name='提货时间')
	or_endTime = models.DateTimeField(verbose_name='计划到达时间')
	or_name = models.CharField(max_length=200,verbose_name='货品名称')
	or_price = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='总价值')
	or_board = models.IntegerField(verbose_name='货板数量')
	or_number = models.IntegerField(verbose_name='数量')
	or_weight = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='总重')
	or_volume = models.CharField(max_length=200,verbose_name='总体积')
	or_truck = models.CharField(max_length=50,verbose_name='货车类型')
	or_length = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='车辆长度')
	or_isDanger = models.BooleanField(verbose_name='是否包含危险品')
	or_isHeap = models.BooleanField(verbose_name='是否可堆放')
	or_isHand = models.BooleanField(verbose_name='是否底板载荷')
	or_isAssist = models.BooleanField(verbose_name='是否需要司机协助装卸工作')
	or_isInsurance = models.BooleanField(verbose_name='是否购买货物保险')
	or_request = models.CharField(max_length=500,verbose_name='其他说明')
	or_status = models.IntegerField(verbose_name='订单状态')

	def __unicode__(self):
		return self.or_id

	class Meta:
		verbose_name = '订单'
		verbose_name_plural = '订单'
