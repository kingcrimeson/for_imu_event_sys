import requests,pprint


payload =  {
               'event_id' : 4,
            'username':'11111111'
            }
response = requests.delete('http://127.0.0.1:8000/api/my_space/I_ve_joined?event_id=4&id=11111111',json=payload)

pprint.pprint(response.json())