from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home,name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^flag', views.about, name='flag'),
    url(r'^api/list/$',views.list, name='list'),
    url(r'^api/listflag/$',views.listflag, name='listflag')
]
