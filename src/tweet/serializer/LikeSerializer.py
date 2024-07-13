from rest_framework import serializers
from tweet.models import Likes

class GetDataLikesFeeds(serializers.ModelSerializer):
	class Meta:
		model = Likes
		fields ='__all__'