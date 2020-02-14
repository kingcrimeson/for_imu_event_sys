"""event_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
import login_register.views
import index.views
import mgr
urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/login',login_register.views.login),
    url('api/logout',login_register.views.logout),
    url('api/register',login_register.views.register),
    url('api/index',index.views.listevent),
    url('api/mgr',include('mgr.urls'))
]
