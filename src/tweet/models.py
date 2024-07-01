from django.db import models
from users.models import Users
from django.utils import timezone

from uuid import uuid4


class Feeds(models.Model):
	users = models.ForeignKey(Users,related_name='users_feeds',on_delete=models.DO_NOTHING)
	content = models.TextField()
	slug = models.CharField(unique=True,max_length=300)
	media = models.FileField(blank=True,upload_to='cdn/')
	retweet = models.BooleanField(default=False)
	likes = models.BigIntegerField(default=0)
	created_at = models.DateTimeField(default=timezone.now())

	def save(self,*args,**kwargs):
		slug = uuid4()
		self.slug = slug
		super(Feeds,self).save(*args,**kwargs)


class Retweet(models.Model):
	users = models.ForeignKey(Users,related_name='users_retweet',on_delete=models.DO_NOTHING)
	feeds = models.ForeignKey(Feeds,related_name='feeds',on_delete=models.DO_NOTHING)
	retwet = models.ForeignKey(Feeds,related_name='retwet',on_delete=models.DO_NOTHING,blank=True)

class Likes(models.Model):
	users = models.IntegerField()
	feeds = models.IntegerField()


