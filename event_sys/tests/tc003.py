import  requests,pprint

response = requests.get('http://127.0.0.1:8000/api/index?action=listevent')

pprint.pprint(response.json())
