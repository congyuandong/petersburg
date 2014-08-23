#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from transport.forms import DriverForm,ClientForm
from transport.models import client,driver

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
	if session:
		return render_to_response('transport/individual.html',context_dict,context)
	else:
		return render_to_response('transport/login.html',context_dict,context)

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
	return render_to_response('transport/individual-orderpublish.html',context_dict,context)

@csrf_exempt
def login(request):
	context = RequestContext(request)
	context_dict = {}
	if request.method == 'POST':
		username = request.POST.get('name')
		password = request.POST.get('pwd')

		client_obj = client.objects.filter(clt_name__exact = username,clt_pwd__exact = password)
		if client_obj:
			request.session['username'] = username
			print	'YES'
			return render_to_response('transport/individual.html',context_dict,context)
		else:
			print 'NO'
			return render_to_response('transport/login.html',context_dict,context)
	return render_to_response('transport/login.html',context_dict,context)

def question(request):
	context = ''
	return render(request,'transport/question.html',context)

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
		return render_to_response('transport/login.html',context_dict,context)
	else:
		return HttpResponse('请先登录')

#货车司机注册
@csrf_exempt 
def driver_reg(request):
	context = RequestContext(request)
	context_dict = {}

	registered = False

	if request.method == 'POST':

		print request.POST
		driverForm = DriverForm(data=request.POST)


		if driverForm.is_valid():
			print 'YES!'
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
