
# Django
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

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
		token = req.headers.get('testing')
		if token is None :
			return Response({"status":403},status=403)
		elif token != settings.KEY_FOR_API:
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
		authorize = req.headers.get('testing')
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

		if Token.objects.filter(user=ambilUser)	.first():
			print(ambilUser.__dict__)
			return Response({"status":401,"message":"Anda Sudah Login"},status=401)

		token = Token.objects.create(user=ambilUser)
		
		data = {
			"status":200,
			"username":ambilUser.username,
			"id_user":ambilUser.id,
			"token":str(token)
		}
		return Response(data)


class LogoutUsers(APIView):
	allowed_methods = 'POST'
	def post(self,req):
		authorize = req.headers.get('testing')
		if authorize is None :
			return Response({"status":403},status=403)
		elif authorize != settings.KEY_FOR_API:
			return Response({"status":401},status=401)

		if "id_users" not in req.data:
			return Response({"status":400,"message":"id_user Di Butuhkan"},status=400)

		user = Users.objects.filter(id=req.data.get('id_users')).first()
		token = Token.objects.filter(user=user).first()
		if user is not None and token is not None:				
			token.delete()
			return Response({"status":200,"message":"Anda Berhasil Logout"})
		return Response({"status":406,"message":"Wrong"},status=406)

class ProfileUsers(APIView):
	allowed_methods = 'GET'
	def get(self,req,pk):
		authorize = req.headers.get('testing')
		if authorize is None :
			return Response({"status":403},status=403)
		elif authorize != settings.KEY_FOR_API:
			return Response({"status":401},status=401)

		user = Users.objects.filter(id=pk).first()
		if user is None:
			return Response({"status":404,"message":"Users Tidak Ditemukan"},status=404)

		#  Mengatur Waktu Date
		waktu = user.created_at.strftime('%d %B %Y')
		jam = user.created_at.strftime('%H:%M')
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
			"jam":jam
		}

		# print(int(round(user.created_at.timestamp())),user.created_at)
		return Response({"status":200,"data":data})

class UpdateProfile(APIView):
	allowed_methods = 'POST'
	def post(self,req,pk):
		authorize = req.headers.get('testing')
		if authorize is None :
			return Response({"status":403},status=403)
		elif authorize != settings.KEY_FOR_API:
			return Response({"status":401},status=401)

		user = Users.objects.filter(id=pk).first()
		if user is None:
			return Response({"status":404},status=404)

		user.username = req.data.get('username')
		user.profile = req.data.get('profile')
		user.name = req.data.get('name')
		user.bio = req.data.get('bio')
		user.save()

		return Response({"status":200})


class FollowUser(APIView):
	allowed_methods = 'GET'
	def get(self,req,pk):
		authorize = req.headers.get('testing')
		if authorize is None :
			return Response({"status":403},status=403)
		elif authorize != settings.KEY_FOR_API:
			return Response({"status":401},status=401)
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



