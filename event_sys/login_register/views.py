from django.shortcuts import render
from django.http import JsonResponse
from . import models
import json
import datetime
# Create your views here.



def login(request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password')
    try:
        user = models.User.objects.get(name=userName)
        if user.password == passWord:
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return JsonResponse({'ret': 0 })
        else:
            msg = '用户名或密码不正确！'
            return JsonResponse({'ret': 1,'msg':msg})
    except:
        msg = '用户名不存在！'
        return JsonResponse({'ret': 1,'msg':msg})


def register(request):
    request.params = json.loads(request.body)
    info = request.params['data']
    username = info['username']
    usernichen = info['nichen']
    password1 = info['password1']
    password2 = info['password2']
    email = info['email']
    if password1 != password2:
        msg = "两次输入的密码不同！"
        return JsonResponse({'ret':1,'msg':msg})
    else:
        same_name_user = models.User.objects.filter(name=username)
        if same_name_user:
            msg = "用户已经存在，请重新选择用户名！"
            return JsonResponse({'ret':1,'msg':msg})
        same_nichen_user = models.User.objects.filter(nichen=usernichen)
        if same_nichen_user:
            msg = "昵称已存在，请更换昵称！"
            return JsonResponse({'ret': 1, 'msg': msg})
        new_user = models.User.objects.create()
        new_user.name = username
        new_user.nichen =usernichen
        new_user.password = password1
        new_user.email = email
        new_user.save()
        return JsonResponse({'ret':0})