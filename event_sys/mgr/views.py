from django.shortcuts import render
from django.http import JsonResponse
from . import models
import json
from index.models import event
import datetime

def list(request):
    qs = models.event.objects.values()
    events = list(qs)
    return JsonResponse({'ret': 0, 'event': events})


def listdetail(request):
    request.params = request.GET
    event_id = request.params['id']
    event_msg = models.event.objects.get(id=event_id)
    event_detail = models.event_details.objects.get(id=event_id)
    user_id = request.session['user_id']
    same_id = models.event_members.objects.filter(id=user_id)
    if same_id:
       whether_or_not = 1
    else :
       whether_or_not = 0
    return JsonResponse({'ret': 0,'whether_or_not':whether_or_not,'event_msg':event_msg,'event_detail':event_detail})


def delete_event(request):
    request.params = json.loads(request.body)
    event_id = request.params['event_id']
    try:
        del_event = event.objects.get(id=event_id)
    except event.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{event_id}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    del_event.delete()

    return JsonResponse({'ret': 0})