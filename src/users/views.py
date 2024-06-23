
# Django
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.http import HttpResponse
import os
################

# Serializer
from users.serializer.SerializerUser import UserSerializer
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



