from django.contrib import admin
from django.conf.urls import url
import login_register.views
import mgr.dispatcher
import mgr.views
urlpatterns = [

    url('list',mgr.dispatcher.dispatch),
    url('listdetail', mgr.dispatcher.dispatch),
    url('delete', mgr.dispatcher.dispatch),
    url('power_give',mgr.dispatcher.dispatch)
]