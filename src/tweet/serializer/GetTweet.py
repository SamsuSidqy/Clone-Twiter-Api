from rest_framework import serializers
from users.serializer.SerializerUser import TweetUsers
from tweet.models import Feeds, Retweet

class GetAllTweet(serializers.ModelSerializer):
	users = TweetUsers()
	class Meta:
		model = Feeds
		fields ='__all__'


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
	class Meta:
		model = Feeds
		fields = '__all__'