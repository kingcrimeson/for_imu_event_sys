from django.shortcuts import render
from django.http import JsonResponse
from . import models
from login_register.models import User
import json
from index.models import event
from django.core.paginator import Paginator, EmptyPage
from django.db.models import F,Q
from django.forms.models import model_to_dict
import datetime

def list(request):
    request.params = request.GET
    try:
        qs = models.event.objects.annotate(events_starter=F('event_starter__nichen')) \
            .values('event_name', 'event_start_time', 'event_end_time', 'event_sign_up_time', 'event_localtion',
                    'event_max_number', 'event_now_number', 'events_starter')
        if qs.none():
            return JsonResponse({'ret': 1, 'msg': '还没有活动'})
        event_nam = request.params.get('event_name', None)
        if event_nam:
            conditions = [Q(event_name__contains=one) for one in event_nam.split(' ') if one]
            query = Q()
            for condition in conditions:
                query &= condition
            qs = qs.filter(query).values()
        pagenum = request.params['pagenum']
        pagesize = request.params['pagesize']
        pgnt = Paginator(qs, pagesize)
        page = pgnt.page(pagenum)
        events = list(page)
        return JsonResponse({'ret': 0, 'event': events, 'total': pgnt.count})
    except EmptyPage:
        return JsonResponse({'ret': 0, 'event': []})

def listdetail(request):
    request.params = request.GET
    event_id = request.params['id']
    try:
         events_msg = models.event.objects.get(id=event_id)
         event_msg = model_to_dict(events_msg)
         events_detail = models.event_details.objects.get(event_name_id=events_msg)
         event_detail=list( events_detail)
         user_id = request.session['user_id']
         same_id = models.event_members.objects.filter(id=user_id)
         if same_id:
              whether_or_not = 1
         else :
              whether_or_not = 0
         return JsonResponse({'ret': 0,'whether_or_not':whether_or_not,'event_msg':event_msg,'event_detail':event_detail})
    except:
         return JsonResponse({'ret':1,'msg':'活动不存在'})

def delete_event(request):
    request.params = json.loads(request.body)
    event_id = request.params['event_id']
    try:
        del_event = event.objects.get(id=event_id)
        del_event.delete()
        return JsonResponse({'ret':0,'msg':'删除成功'})
    except:
        return JsonResponse({
            'ret': 1,
            'msg': f'id 为`{event_id}`的活动不存在'
        })

    return JsonResponse({'ret': 0})


def power_give(request):
    request.params = json.loads(request.body)
    username = request.params['username']
    try:
        user = User.objects.get(name=username)
        user.permission = 1
        user.save()
        return JsonResponse({'ret':0})
    except:
        return JsonResponse({'ret':1,'msg':'用户不存在'})
