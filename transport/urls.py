from django.conf.urls import patterns, url
from transport import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),
	url(r'^download', views.download, name='download'),
	url(r'^about', views.about, name='about'),
	url(r'^individual', views.individual, name='individual'),
	url(r'^i/list', views.orderlist, name='orderlist'),
	url(r'^i/detail', views.orderdetail, name='orderdetail'),
	url(r'^i/publish', views.orderpublish, name='orderpublish'),
	url(r'^login', views.login, name='login'),
	url(r'^question', views.question, name='question'),
	url(r'^reg', views.reg, name='reg'),
	url(r'^driver_reg',views.driver_reg,name='driver_reg'),
	url(r'^logout',views.logout,name='logout'),
	)