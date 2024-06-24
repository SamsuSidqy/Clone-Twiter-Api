
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
import os
################

# Serializer
from users.serializer.SerializerUser import UserSerializer
#######

# Model
from users.models import Users
#######

import json

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
		token = req.headers.get('testing')
		if token is None :
			return Response({"status":403},status=403)
		elif token != settings.KEY_FOR_API:
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
		print(token)
		data = {
			"status":200,
			"username":ambilUser.username,
			"id_user":ambilUser.id,
			"token":str(token)
		}
		return Response(data)


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



