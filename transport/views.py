#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from transport.forms import DriverForm,ClientForm
from transport.models import client,driver,order

import simplejson as json

def index(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('transport/index.html',context_dict,context)

def download(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('transport/download.html',context_dict,context)

def about(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('transport/about.html',context_dict,context)

#个人中心
def individual(request):
	context = RequestContext(request)
	context_dict = {}
	session = request.session.get('username',False)
	if not session:
		return render_to_response('transport/login.html',context_dict,context)
	order_objs = order.objects.all()
	context_dict['orders'] = order_objs
	print context_dict
	return render_to_response('transport/individual.html',context_dict,context)

#订单列表
def orderlist(request):
	context = RequestContext(request)
	context_dict = {}	
	return render_to_response('transport/individual.html',context_dict,context)

#订单详情
def orderdetail(request):
	context = RequestContext(request)
	context_dict = {}	
	return render_to_response('transport/individual-orderdetail.html',context_dict,context)

#订单发布
def	orderpublish(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		print request.POST

	return render_to_response('transport/individual-orderpublish.html',context_dict,context)

def question(request):
	context = ''
	return render(request,'transport/question.html',context)

@csrf_exempt
def login(request):
	context = RequestContext(request)
	context_dict = {}
	if request.method == 'POST':
		mail = request.POST.get('name')
		password = request.POST.get('pwd')

		client_obj = client.objects.get(clt_mail__exact = mail,clt_pwd__exact = password)
		if client_obj:
			request.session['username'] = client_obj.clt_name
			request.session['user_id'] = client_obj.id
			print '用户登录成功'
			return render_to_response('transport/individual.html',context_dict,context)
		else:
			print '用户登录失败'
			return render_to_response('transport/login.html',context_dict,context)
	return render_to_response('transport/login.html',context_dict,context)

@csrf_exempt 
def reg(request):
	context = RequestContext(request)
	context_dict = {}
	registered = False

	if request.method == 'POST':
		print request.POST
		print request.POST.get('clt_industry')

		clientForm = ClientForm(data=request.POST)

		if clientForm.is_valid():
			print '注册成功'
			registered = True
			clientForm.save()
			return render_to_response('transport/login.html',context_dict,context)
		else:
			print clientForm.errors
		
	context_dict['registered'] = registered
	return render_to_response('transport/reg.html',context_dict,context)

def logout(request):
	context = RequestContext(request)
	context_dict = {}

	session = request.session.get('username',False)
	if session:
		del request.session['username']
		del request.session['user_id']
		return render_to_response('transport/login.html',context_dict,context)
	else:
		return HttpResponse('请先登录')

#司机获取固定范围内订单信息，包括车辆的经度维度,货物名称，装车地点，卸车地点
def get_order(request):
	context_list = []
	longitude = request.GET.get('longitude','')
	latitude = request.GET.get('latitude','')
	print longitude,latitude
	order_objs = order.objects.all()[:100]
	print order_objs
	for order_obj in order_objs:
		context = {}
		context['or_id'] = order_obj.or_id
		context['or_name'] = order_obj.or_name
		context['or_longitude'] = order_obj.or_longitude
		context['or_latitude'] = order_obj.or_latitude
		context['or_start'] = order_obj.or_start
		context['or_end'] = order_obj.or_end
		context_list.append(context)
	print context_list
	return HttpResponse(json.dumps(context_list),content_type="application/json")

#获取订单详细信息
def get_order_detail(request):
	context = []
	if request.method == 'GET':
		or_id = request.GET.get('or_id','')
		order_obj = order.objects.filter(or_id__exact = or_id)
		context = json.loads(serializers.serialize("json", order_obj))[0]['fields']
		order_obj = order.objects.get(or_id__exact = or_id)
		order_obj.or_view = order_obj.or_view+1
		order_obj.save()
	print context
	return HttpResponse(json.dumps(context),content_type="application/json")

#货车司机注册
@csrf_exempt 
def driver_reg(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		print request.POST
		driverForm = DriverForm(data=request.POST)

		if driverForm.is_valid():
			print '司机注册成功'
			driverForm.save()
			context_dict['status']='1'
		else:
			print driverForm.errors
			context_dict['status']='0'

	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#货车司机注册 WEB端
@csrf_exempt 
def dreg(request):
	context = RequestContext(request)
	context_dict = {}

	registered = False

	if request.method == 'POST':

		print request.POST
		driverForm = DriverForm(data=request.POST)


		if driverForm.is_valid():
			print '司机注册成功'
			driverForm.save()
			registered = True
		else:
			print driverForm.errors

	else:
		driverForm = DriverForm()

	context_dict['driverForm'] = driverForm
	context_dict['registered'] = registered

	return	render_to_response('transport/driver_reg.html',context_dict,context)

#货车司机登录
@csrf_exempt
def driver_login(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		telphone = request.POST.get('dr_tel')
		password = request.POST.get('dr_pwd')
		#print	telphone,password
		driver_obj = driver.objects.filter(dr_tel__exact = telphone,dr_pwd__exact = password)
		if driver_obj:
			print	'司机登录成功'
			context_dict['status']='1'
			context_dict['data']=json.loads(serializers.serialize("json", driver_obj))[0]['fields']
		else:
			print	'司机登录失败'
			context_dict['status']='0'
	print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#货车司机修改密码
@csrf_exempt
def driver_pwd(request):
	context_dict = {}
	
	if request.method == 'POST':
		dr_tel = request.POST.get('dr_tel')
		dr_pwd = request.POST.get('dr_pwd')

		driver_obj = driver.objects.get(dr_tel__exact = dr_tel)
		if driver_obj:
			driver_obj.dr_pwd = dr_pwd
			driver_obj.save()
			context_dict['status']='1'
			print '司机密码修改成功'
		else:
			context_dict['status']='0'
			print '司机密码修改失败'
	print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#货车信息修改
@csrf_exempt
def driver_update(request):
	context_dict = {}

	if request.method == 'POST':
		dr_tel = request.POST.get('dr_tel')
		dr_number = request.POST.get('dr_number')
		dr_hand = request.POST.get('dr_hand')
		dr_type = request.POST.get('dr_type')
		dr_length = request.POST.get('dr_length')
		dr_weight = request.POST.get('dr_weight')

		driver_obj = driver.objects.get(dr_tel__exact = dr_tel)

		if driver_obj:
			driver_obj.dr_number = dr_number
			driver_obj.dr_hand = dr_hand
			driver_obj.dr_type = dr_type
			driver_obj.dr_length = dr_length
			driver_obj.dr_weight = dr_weight
			driver_obj.save()
			context_dict['status']='1'
			print '车辆信息修改成功'
		else:
			context_dict['status']='0'
			print '车辆信息修改失败'

	print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

