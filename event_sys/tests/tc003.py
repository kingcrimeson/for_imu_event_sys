import requests,pprint
import json
url='http://127.0.0.1:8000/api/details?action=listevent_details&id=1'
response = requests.get(url=url,)

pprint.pprint(response.json())
