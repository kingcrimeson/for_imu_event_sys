from django.shortcuts import render
from django.http import JsonResponse
from index import models
import json
from django.db import transaction
from index.models import event,event_members,event_details
from login_register.models import User
from django.core import serializers
from django.db.models import F


def list_event(request):
    request.params = request.GET
    user_id = request.params['id']
    id = User.objects.get(id=user_id)
    qs = models.event.objects.filter(event_starter=id).values()
    events=list(qs)
    return JsonResponse({'ret':0,'event':events})


def hold_event(request):
    request.params = json.loads(request.body)
    info = request.params['event']
    event_name = info['event_name']
    event_start_time = info['event_start_time']
    event_end_time = info['event_end_time']
    event_sign_up_time = info['event_sign_up_time']
    event_localtion = info['event_localtion']
    event_now_number = info['event_now_number']
    event_max_number = info['event_max_number']
    event_detail = info['event_detail']
    s_nichen = request.params['nichen']
    id = models.User.objects.get(nichen=s_nichen)
    with transaction.atomic():
        new_event = event.objects.create()
        new_event.event_starter=id
        new_event.event_max_number=event_max_number
        new_event.event_now_number=event_now_number
        new_event.event_end_time=event_end_time
        new_event.event_localtion=event_localtion
        new_event.event_sign_up_time=event_sign_up_time
        new_event.event_name=event_name
        new_event.event_start_time=event_start_time
        new_event.save()
        new_eventdetails=event_details.objects.create()
        new_eventdetails.event_name=new_event
        new_eventdetails.event_detail=event_detail
        new_eventdetails.save()
        return JsonResponse({'ret':0,'msg':'发起成功'})
    return JsonResponse({'ret' : 1,'msg' : '发起活动失败，请再试一遍'})


def event_joined(request):
    if request.method == 'GET':
        request.params = request.GET
        try:
             username = request.params['id']
             user = User.objects.get(name=username)
             qs = event_members.objects.filter(member_id=user) \
                .annotate(
                event_name=F('event_id__event_name'),
                event_start_time=F('event_id__event_start_time'),
                event_end_time=F('event_id__event_end_time'),
                event_sign_up_time=F('event_id__event_sign_up_time'),
                event_localtion=F('event_id__event_localtion'),
                events_id =F('event_id__id')
                   ) \
                .values('events_id', 'event_name', 'event_start_time', 'event_end_time', 'event_sign_up_time', 'event_localtion')
             events = list(qs)
             return JsonResponse({'ret': 0, 'event': events})
        except:
             return JsonResponse({'ret':1,'msg':'你还没有参与活动'})
    elif request.method == 'DELETE':

        request.params = json.loads(request.body)
        username = request.params['username']
        eventid = request.params['event_id']
        nichen = User.objects.get(name=username)
        try:
             event = models.event.objects.get(id=eventid)
             member = event_members.objects.filter(event_id=event,member_nichen=nichen)
             member.delete()
             ret = 0
             msg = '退出成功'
        except:
             ret = 1
             msg = '退出失败'
        return JsonResponse({'ret':ret,'msg':msg})