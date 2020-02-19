from django.shortcuts import render
from . import models
import json
from django.http import JsonResponse
from login_register.models import User
# Create your views here.


def listevent(request):
    if 'is_login' not in request.session:
        msg = '请先登录'
        return JsonResponse({'ret': 1, 'msg': msg})
    qs = models.event.objects.values()
    if qs.none():
        return JsonResponse({'ret': 1,'msg':'还没有活动'})
    events = list(qs)
    return JsonResponse({'ret':0,'event':events})


def listevent_details(request):
    if 'is_login' not in request.session:
        msg = '请先登录'
        return JsonResponse({'ret': 1, 'msg': msg})
    if request.method == 'GET':
        request.params = request.GET
        event_id = request.params['id']
        event_msg = models.event.objects.filter(id=event_id)
        if not event_msg:
            return JsonResponse({'ret': 0, 'msg': '该活动不存在'})
        event_detail = models.event_details.objects.get(id=event_id)
        user_id = request.session['user_id']
        same_id = models.event_members.objects.filter(id=user_id)
        if same_id:
            whether_or_not = 1
        else :
            whether_or_not = 0
        return JsonResponse({'ret': 0,'whether_or_not':whether_or_not,'event_msg':event_msg,'event_detail':event_detail})

    elif request.method == 'POST':
        request.params = json.loads(request.body)
        info = request.params['data']
        event_id = request.params['event_id']
        event = models.event.objects.get(id=event_id)
        if event.event_now_number<event.event_max_number:
            event.event_now_number = event.event_now_number + 1
            new_joiner = models.event_members.objects.create()
            new_joiner.member_nichen = info['nichen']
            new_joiner.member_real_name = info['real_name']
            new_joiner.member_tel = info['tel']
            new_joiner.member_qq = info['qq']
            new_joiner.member_id = User.objects.get(nichen=info['nichen'])
            new_joiner.event_id = event
            new_joiner.save()
            msg = '报名成功'
        else:
            msg = '人数已满'
        return JsonResponse({'ret':1,'msg':msg})
