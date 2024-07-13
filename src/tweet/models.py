from django.db import models
from users.models import Users
from datetime import datetime




class Feeds(models.Model):
	users = models.ForeignKey(Users,related_name='users_feeds',on_delete=models.DO_NOTHING)
	content = models.TextField()
	slug = models.TextField(unique=True,max_length=300)
	media = models.FileField(blank=True,upload_to='cdn/')
	retweet = models.BooleanField(default=False)
	likes = models.BigIntegerField(default=0)
	created_at = models.DateTimeField(blank=True)

	class Meta:
		ordering = ['-created_at']
	


class Retweet(models.Model):
	users = models.ForeignKey(Users,related_name='users_retweet',on_delete=models.DO_NOTHING)
	feeds = models.ForeignKey(Feeds,related_name='feeds',on_delete=models.DO_NOTHING)
	retwet = models.ForeignKey(Feeds,related_name='retwet',on_delete=models.DO_NOTHING,blank=True)

class Likes(models.Model):
	users = models.IntegerField()
	feeds = models.IntegerField()


