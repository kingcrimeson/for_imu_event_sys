from django.db import models
import login_register

# Create your models here.
class event(models.Model):
      event_name = models.CharField(max_length=200)
      event_start_time = models.CharField(max_length=50)
      event_end_time = models.CharField(max_length=50)
      event_sign_up_time = models.CharField(max_length=50)
      event_localtion = models.CharField(max_length=200)
      event_max_number = models.IntegerField(null=True)
      event_now_number = models.IntegerField(null=True)
      event_starter = models.ForeignKey(login_register.models.User, on_delete=models.CASCADE,null = True,related_name = 'starter')
      event_mem = models.ManyToManyField(login_register.models.User,through='event_members',null = True,related_name='man_joined')
class event_details(models.Model):
      event_name = models.OneToOneField(event,on_delete=models.CASCADE,null=True)
      event_detail = models.TextField(null= True)
class event_members(models.Model):
      event_id = models.ForeignKey(event,on_delete=models.CASCADE,null=True)
      member_id = models.ForeignKey(login_register.models.User,on_delete=models.CASCADE,null=True)
      member_nichen = models.CharField(max_length=50)
      member_real_name = models.CharField(max_length=50)
      member_tel = models.CharField(max_length=50)
      member_qq = models.CharField(max_length=50)