from django.contrib import admin
from django.conf.urls import url
import login_register.views
import mgr.dispatcher
urlpatterns = [

    url('list',mgr.dispatcher.dispatch),
    url('listdetail', mgr.dispatcher.dispatch),
    url('delete', mgr.dispatcher.dispatch),
]