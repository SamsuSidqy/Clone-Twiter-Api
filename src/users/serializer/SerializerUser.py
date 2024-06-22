# Django & Rest
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.validators import UniqueValidator

# Model
from users.models import Users


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = Users
		fields = ('username','password','email','id','profile','created_at')
		extra_kwargs ={
			"username":{
				"error_messages":{
					"required":"Username Di Perlukan",
					"blank":"Username Tidak Boleh Kosong",
					"max_length":"Username Maksimal 150 Karakter",
				}		
			},
			"email":{
				"error_messages":{
					"required":"Email Di Perlukan",
					"blank":"Email Tidak Boleh Kosong",
					"max_length":"Email Maksimal 150 Karakter",
				}
			},
			"password":{
				"error_messages":{
					"required":"Password Di Perlukan",
				}
			}
		}

	def create(self,validated_data):
		pswd = validated_data.get('password')
		print(pswd)
		hasing = make_password(pswd)
		validated_data['password'] = hasing
		return super().create(validated_data)

	

