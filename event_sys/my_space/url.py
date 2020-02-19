from django.contrib import admin
from django.conf.urls import url
import login_register.views
import my_space.views
urlpatterns = [

    url('index',my_space.views.list_event),
    url('hold_event',my_space.views.hold_event),
    url('I_ve_joined',my_space.views.event_joined),
]