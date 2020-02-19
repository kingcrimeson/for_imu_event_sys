import  requests,pprint

url ='http://127.0.0.1:8000/api/details?action=listevent'
data =  {
                                                              	          "action" : "sign_up",
                                                                          "event_id":4,
                                                                          "data" : {
                                                                                   "nichen" : "阿健",
                                                                                   "real_name" : "周健",
                                                                                   "tel" : "136xxxxxxxx",
                                                                                   "qq" : "616094580",
                                                                                      }
                                                           }
response = requests.post(url=url,json=data)
pprint.pprint(response.json())