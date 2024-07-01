
# Django
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from oauth2_provider.models import AccessToken
from oauthlib.common import generate_token 	
from oauth2_provider.contrib.rest_framework import TokenHasResourceScope, TokenHasScope, OAuth2Authentication
################

# Serializer
from users.serializer.SerializerUser import UserSerializer
#######

# Model
from users.models import Users,Followers
#######

import json
import os
from datetime import datetime

class CreateUser(CreateAPIView):
	serializer_class = UserSerializer
	renderer_classes = [JSONRenderer]
	allowed_methods = 'POST'
	def create(self,req,*args,**kwargs):
		authorize = req.headers.get(settings.HEADER_KEY)
		if authorize is None :
			return Response({"status":403},status=403)
		elif authorize != settings.KEY_FOR_API:
			return Response({"status":401},status=401)
		serializer = self.serializer_class(data=req.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer)
		return Response(serializer.data, status=200, headers=headers)

	def perform_create(self, serializer):
		serializer.save()

	def get_success_headers(self, data):
		try:
			return {'Message':  data[api_settings.URL_FIELD_NAME]}
		except Exception as e:
			return {'Errors':e}


class LoginUsers(APIView):
	def post(self,req):
		authorize = req.headers.get(settings.HEADER_KEY)
		if authorize is None :
			return Response({"status":403},status=403)
		elif authorize != settings.KEY_FOR_API:
			return Response({"status":401},status=401)
		elif "username" not in req.data or "password" not in req.data:
			return Response({"status":400,"Message":"Username & Password Required"},status=400)

		username = req.data.get('username')
		password = req.data.get('password')

		ambilUser = Users.objects.filter(username=username).first()
		if ambilUser is None:
			return Response({"status":404,"message":"Username / Password Salah"},status=404)

		if check_password(password,ambilUser.password) is False:
			return Response({"status":404,"message":"Username / Password Salah"},status=404)
		
		
		checkingToken = AccessToken.objects.filter(user=ambilUser).first()

		if checkingToken:
			return Response({"status":401,"message":"Anda Sudah Login"})
		token = generate_token()
		createToken = AccessToken.objects.create(user=ambilUser,expires=datetime(2024,7,30),token=token)
		data = {
			"status":200,
			"username":ambilUser.username,
			"id_user":ambilUser.id,
			"token_bearer":createToken.token,
			'expires':createToken.expires,
		}
		return Response(data)


class LogoutUsers(APIView):
	allowed_methods = 'POST'	
	authentication_classes  = [OAuth2Authentication]
	permission_classes = [TokenHasResourceScope]
	def post(self,req):		
		if "id_users" not in req.data:
			return Response({"status":400,"message":"id_users Di Butuhkan"},status=400)

		user = Users.objects.filter(id=req.data.get('id_users')).first()
		token = AccessToken.objects.filter(user=user).first()
		if user is not None and token is not None:				
			token.delete()
			return Response({"status":200,"message":"Anda Berhasil Logout"})
		return Response({"status":406,"message":"Wrong"},status=406)

class ProfileUsers(APIView):
	allowed_methods = 'GET'
	authentication_classes  = [OAuth2Authentication]
	permission_classes = [TokenHasResourceScope]
	def get(self,req,pk):		
		user = Users.objects.filter(username=pk).first()
		if user is None:
			return Response({"status":404,"message":"Users Tidak Ditemukan"},status=404)
		token = AccessToken.objects.filter(user=user).first()		
		print(user.created_at.ctime())	
		#  Mengatur Waktu Date
		waktu = user.created_at.strftime('%d %B %Y')	
		cekrequest = req.headers.get('Authorization') == f"Bearer {token}"
		data ={
			"username":user.username,
			"id_users":user.id,
			"name":user.name,
			"verify":user.verify,
			"email":user.email,
			"profile":user.profile.url if user.profile else None,
			"bio":user.bio,
			"follow":user.follow,
			"date_joined":waktu,
			"token_bearer":token.token if cekrequest else 'Forbidden',
			"expires_token"	:token.expires if cekrequest else 'Forbidden',
		}

		# print(int(round(user.created_at.timestamp())),user.created_at)
		return Response({"status":200,"data":data})

class UpdateProfile(APIView):
	authentication_classes  = [OAuth2Authentication]
	permission_classes = [TokenHasResourceScope]

	def post(self,req,pk):		
		user = Users.objects.filter(id=pk).first()
		if user is None:
			return Response({"status":404},status=404)

		if "username" in req.data:
			user.username = req.data.get('username').replace(" ","").lower()
		if "profile" in req.data:
			user.profile = req.data.get('profile')
		if "name" in req.data:
			user.name = req.data.get('name')
		if "bio" in req.data:
			user.bio = req.data.get('bio')
		user.save()

		return Response({"status":200})


class FollowUser(APIView):
	allowed_methods = 'GET'
	authentication_classes  = [OAuth2Authentication]
	permission_classes = [TokenHasResourceScope]
	def get(self,req,pk):
		
		userToFollow = Users.objects.filter(id=req.data.get('id_users')).first()
		followToUser = Users.objects.filter(id=pk).first()
		if userToFollow is not None and followToUser is not None:
			cek = Followers.objects.filter(userfollow=followToUser.id,followuser=userToFollow.id).first()
			if cek is None:
				Followers.objects.create(userfollow=followToUser.id,followuser=userToFollow.id).save()
				userToFollow.follow += 1			
			else: 
				if userToFollow.follow > 0:
					userToFollow.follow -= 1
				cek.delete()
			userToFollow.save()

			return Response({"status":200,"message":"Follow Sukses"})
		return Response({"status":404,"message":"Ada Yang Salah Dari Id User"})


class CekDokumen(APIView):

	def get(self,request,id):
		if id != '66b7d80f-5507-4512-9246-9ad273eab6a4':
			return HttpResponse("Hayyuu Mau Ngapain")
		pwd = os.path.join(settings.BASE_DIR)
		with open(f"{pwd}/src/dokumen/a.pdf",'rb') as pdf:
			respon = HttpResponse(pdf.read(),content_type='application/pdf')
			return respon
		pdf.closed

		# return HttpResponse('<h1>Hello World</h1>')



