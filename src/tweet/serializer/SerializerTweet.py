from rest_framework import serializers

from tweet.models import Feeds

class TweetSerializer(serializers.ModelSerializer):		

	class Meta:
		model = Feeds
		fields = ['users','content','media','retwet','retweet']
		extra_kwargs = {
			"users":{
				"error_messages":{
					"required":"Users Di Butuhkan",
					"blank":"Users Tidak Boleh Blank"
				}
			},
			"content":{
				"error_messages":{
					"required":"Content Di Butuhkan",
					"blank":"Content Tidak Boleh Blank"
				}
			},
			"retwet":{
				"required":False
			}
		}
	