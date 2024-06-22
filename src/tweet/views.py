# Django
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
################

#Serialzer
from tweet.serializer.SerializerTweet import TweetSerializer
from tweet.serializer.SerializerRetweet import RetweetSerializer

from tweet.serializer.GetTweet import GetAllTweet,GetRetweet
################

#Models
from tweet.models import Feeds, Retweet, Likes
from users.models import Users
################

class PostingTweet(CreateAPIView):
	serializer_class = TweetSerializer
	renderer_classes = [JSONRenderer]
	allowed_methods = 'POST'
	def create(self,req,*args,**kwargs):
		serializer = self.serializer_class(data=req.data)
		serializer.is_valid(raise_exception=True)
		instance = serializer.save()
		if "typeretwet" in req.data and req.data['typeretwet']:
			user = Users.objects.filter(id=req.data['users']).first()
			retweet =  Feeds.objects.filter(id=req.data['wheretweet']).first()
			objek = Retweet.objects.create(
					users=user,
					feeds=instance,
					retwet=retweet,
				)
			objek.save()

		headers = self.get_success_headers(serializer)
		return Response(serializer.data, status=200, headers=headers)

	def perform_create(self, serializer):
		serializer.save()

	def get_success_headers(self, data):
		try:
			return {'Message':  data[api_settings.URL_FIELD_NAME]}
		except Exception as e:
			return {'Errors':e}



class TweetAll(ListAPIView):
	serializer_class = GetAllTweet
	renderer_classes = [JSONRenderer]
	model = Feeds
	queryset = Feeds.objects.filter(retweet=False)
	# a = Retweet.objects.filter(retwet__id=2)
	# print(queryset)
	# print(a)

class RetweetAll(ListAPIView):
	serializer_class = GetRetweet
	renderer_classes = [JSONRenderer]
	models = Retweet
	# queryset = Retweet.objects.all()

	def get_queryset(self):
		idd = self.kwargs.get('num')
		queryset = Retweet.objects.filter(retwet_id=idd)						
		return queryset
		

class LikeFeeds(APIView):	
	allowed_methods = 'GET'
	def get(self,req,pk,author):
		try:
			objek = Feeds.objects.get(id=pk)
			ceklike = Likes.objects.filter(users=author,feeds=pk).first()
			if ceklike is None:
				objek.likes += 1
				Likes.objects.create(users=author,feeds=pk).save()			
				objek.save()
			return Response({"message":200},status=200)
		except Feeds.DoesNotExist:
			return Response({"message":404},status=404)


class UnlikeFeeds(APIView):
	allowed_methods = 'GET'
	def get(self,req,pk,author):
		try:
			objek = Feeds.objects.get(id=pk)
			ceklike = Likes.objects.filter(users=author,feeds=pk).first()
			if objek.likes > 0 and ceklike:
				objek.likes -= 1
				ceklike.delete()
				objek.save()
			return Response({"message":200},status=200)
		except Feeds.DoesNotExist:
			return Response({"message":404},status=404)



