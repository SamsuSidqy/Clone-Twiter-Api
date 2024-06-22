from rest_framework import serializers

from tweet.models import Feeds, Retweet

class GetAllTweet(serializers.ModelSerializer):
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