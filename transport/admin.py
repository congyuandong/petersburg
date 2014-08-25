#coding:utf-8
from django.contrib import admin
from transport.models import client,driver,order,offer

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
	fields = ['clt_name','clt_pwd','clt_mail','clt_tel','clt_company','clt_position','clt_industry','clt_from']
	list_display = ['clt_name','clt_pwd','clt_mail','clt_tel','clt_company','clt_position','clt_industry','clt_from']
	search_fields = ['clt_name']

class DriverAdmin(admin.ModelAdmin):
	fields = ['dr_name','dr_iden','dr_tel','dr_number','dr_hand','dr_type','dr_length','dr_weight','dr_pwd']
	list_display = ['dr_name','dr_iden','dr_tel','dr_number','dr_hand','dr_type','dr_length','dr_weight','dr_pwd']
	search_fields = ['dr_name']

class OrderAdmin(admin.ModelAdmin):
	fields = ['or_client','or_id','or_update','or_title','or_start','or_end','or_startTime','or_endTime','or_name','or_price','or_board','or_number','or_weight','or_volume','or_truck','or_length','or_isDanger','or_isHeap','or_isHand','or_isAssist','or_isInsurance','or_request','or_status','or_longitude','or_latitude','or_view']
	list_display = ['or_client','or_id','or_update','or_title','or_start','or_end','or_startTime','or_endTime','or_name','or_price','or_board','or_number','or_weight','or_volume','or_truck','or_length','or_isDanger','or_isHeap','or_isHand','or_isAssist','or_isInsurance','or_request','or_status','or_longitude','or_latitude','or_view']
	search_fields = ['or_name']
	
class OfferAdmin(admin.ModelAdmin):
	fields = ['of_order','of_driver','of_price']
	list_display = ['of_order','of_driver','of_price']
	search_fields = ['of_order']

admin.site.register(client,ClientAdmin)
admin.site.register(driver,DriverAdmin)
admin.site.register(order,OrderAdmin)
admin.site.register(offer,OfferAdmin)