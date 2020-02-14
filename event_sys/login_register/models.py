from django.db import models

class User(models.Model):
    '''用户表'''

    name = models.CharField(max_length=128, unique=True)
    nichen = models.CharField(max_length=128,unique=True,null=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    permission = models.IntegerField(null=True)
