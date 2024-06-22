from rest_framework import serializers

from tweet.models import Feeds, Retweet

class GetAllTweet(serializers.ModelSerializer):
	class Meta:
		model = Feeds
		fields ='__all__'


class GetRetweet(serializers.ModelSerializer):
	class Meta:
		model = Retweet
		fields ='__all__'	