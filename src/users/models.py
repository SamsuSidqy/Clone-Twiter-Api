from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
	username = models.CharField(max_length=150,unique=True,error_messages={"unique":"Username Sudah Terpakai"})
	email = models.CharField(max_length=150,unique=True,error_messages={"unique":"Email Sudah Terpakai"})
	profile = models.TextField(blank=True)
	password = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)


class Bio(models.Model):
	bio = models.TextField(blank=True)
	users = models.ForeignKey(Users,related_name='users_bio',on_delete=models.DO_NOTHING)