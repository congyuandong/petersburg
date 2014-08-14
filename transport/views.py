#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

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