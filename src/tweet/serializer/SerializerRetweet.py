from rest_framework import serializers
from tweet.models import Retweet

class RetweetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Retweet
		fields = ['users','feeds','retwet']
		extra_kwargs = {
			"users":{
				"error_messages":{
					"required":"Users Di Butuhkan",
					"blank":"Users Tidak Boleh Blank"
				}
			},
			"feeds":{
				"error_messages":{
					"required":"feeds Di Butuhkan",
					"blank":"feeds Tidak Boleh Blank"
				}
			},
			"retwet":{
				"error_messages":{
					"required":"retwet Di Butuhkan",
					"blank":"retwet Tidak Boleh Blank"
				}
			}
		}

