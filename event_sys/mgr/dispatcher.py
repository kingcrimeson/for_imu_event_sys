import json
import mgr.views
from django.http import JsonResponse
def dispatch(request):
    if request.session['permission'] < 1:
        return JsonResponse({
            'ret': 302,
            'msg': '用户没有权限',
              },
            status=302)


    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)

    action = request.params['action']
    if action == 'listevent':
        return mgr.views.list(request)
    elif action == 'listdetail':
        return mgr.views.listdetail(request)
    elif action == 'delete':
        return mgr.views.delete_event(request)