from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class Users(AbstractUser):
	username = models.CharField(max_length=150,unique=True,error_messages={"unique":"Username Sudah Terpakai"})
	name = models.CharField(max_length=150,blank=True)
	verify = models.BooleanField(default=False)
	email = models.CharField(max_length=150,unique=True,error_messages={"unique":"Email Sudah Terpakai"})
	profile = models.FileField(blank=True,upload_to='profile/')
	bio = models.TextField(blank=True)
	password = models.TextField()
	follow = models.BigIntegerField(default=0)
	created_at = models.DateTimeField(blank=True,default=datetime.now())

	def save(self,*args,**kwargs):
		username = self.username.replace(" ","").lower()
		self.username = username
		super(Users,self).save(*args,**kwargs)
	


class Followers(models.Model):
	userfollow = models.BigIntegerField(blank=True)
	followuser = models.BigIntegerField(blank=True)
