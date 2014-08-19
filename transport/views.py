#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from transport.forms import DriverForm

def index(request):
	context = ''
	return render(request,'transport/index.html',context)

def download(request):
	context = ''
	return render(request,'transport/download.html',context)

def about(request):
	context = ''
	return render(request,'transport/about.html',context)

def individual(request):
	context = ''
	return render(request,'transport/individual.html',context)

def login(request):
	context = ''
	return render(request,'transport/login.html',context)

def question(request):
	context = ''
	return render(request,'transport/question.html',context)

def reg(request):
	context = ''
	return render(request,'transport/reg.html',context)

def action_reg(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		print request.POST

	return render_to_response(
        'transport/reg.html',
        context_dict,
        context)

def driver_reg(request):
	context = RequestContext(request)
	context_dict = {}

	registered = False

	if request.method == 'POST':

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