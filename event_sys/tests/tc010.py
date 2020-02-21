import  requests,pprint




response = requests.get('http://127.0.0.1:8000/api/index?pagesize=4&pagenum=1&event_name=啦')

pprint.pprint(response.json())