import  requests,pprint




response = requests.get('http://127.0.0.1:8000/api/index?pagesize=1&pagenum=1')

pprint.pprint(response.json())