#coding:utf-8
from django.contrib import admin
from transport.models import client,driver

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
	fiedls = ['clt_name','clt_pwd','clt_mail','clt_tel','clt_company','clt_position','clt_industry','clt_from']
	list_display = ['clt_name','clt_pwd','clt_mail','clt_tel','clt_company','clt_position','clt_industry','clt_from']

class DriverAdmin(admin.ModelAdmin):
	fiedls = ['dr_name','dr_iden','dr_tel','dr_number','dr_hand','dr_type','dr_length','dr_weight','dr_pwd']
	list_display = ['dr_name','dr_iden','dr_tel','dr_number','dr_hand','dr_type','dr_length','dr_weight','dr_pwd']


admin.site.register(client,ClientAdmin)
admin.site.register(driver,DriverAdmin)