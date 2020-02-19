import json
import my_space.views
from django.http import JsonResponse
def dispatch(request):
    #if 'is_login' not in request.session:
     #   msg = '请先登录'
      #  return JsonResponse({'ret': 1, 'msg': msg})

    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)

    action = request.params['action']
    if action == 'listevent':
        return my_space.views.list(request)
    elif action == 'listdetail':
        return my_space.views.listdetail(request)
    elif action == 'delete':
        return my_space.views.delete_event(request)