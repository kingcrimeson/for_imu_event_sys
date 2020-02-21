import  requests,pprint

response = requests.get('http://127.0.0.1:8000/api/my_space/details?id=8')

pprint.pprint(response.json())