from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
	username = models.CharField(max_length=150,unique=True,error_messages={"unique":"Username Sudah Terpakai"})
	name = models.CharField(max_length=150,blank=True)
	verify = models.BooleanField(default=False)
	email = models.CharField(max_length=150,unique=True,error_messages={"unique":"Email Sudah Terpakai"})
	profile = models.TextField(blank=True)
	bio = models.TextField(blank=True)
	password = models.TextField()
	follow = models.BigIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)


class Followers(models.Model):
	userfollow = models.BigIntegerField(blank=True)
	followuser = models.BigIntegerField(blank=True)
