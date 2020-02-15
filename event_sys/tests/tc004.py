import  requests,pprint

response = requests.get('http://127.0.0.1:8000/api/logout?action=listevent_details&id=1')

pprint.pprint(response.json())