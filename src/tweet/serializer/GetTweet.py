from rest_framework import serializers
from users.serializer.SerializerUser import TweetUsers
from tweet.models import Feeds, Retweet
from datetime import datetime

class GetAllTweet(serializers.ModelSerializer):
	users = TweetUsers()
	created_at = serializers.SerializerMethodField()
	class Meta:
		model = Feeds
		fields ='__all__'

	def get_created_at(self,obj):	
		print(obj.created_at)
		# print(datetime.now())
		return obj.created_at.strftime("%d %B %Y, %H:%M")


class GetRetweet(serializers.ModelSerializer):
	retwet = GetAllTweet()	
	feeds = GetAllTweet()
	class Meta:
		model = Retweet
		fields ='__all__'

class LikeTweet(serializers.ModelSerializer):
	class Meta:
		model = Feeds
		fields = ['likes']

class SingleTweet(serializers.ModelSerializer):
	users = TweetUsers()
	created_at = serializers.SerializerMethodField()
	class Meta:
		model = Feeds
		fields = '__all__'

	def get_created_at(self,obj):		
		return obj.created_at.strftime("%d %B %Y, %H:%M")

class TweetAllRetweet(serializers.ModelSerializer):
	class Meta:
		model = Feeds
		fields = ['id','content']



