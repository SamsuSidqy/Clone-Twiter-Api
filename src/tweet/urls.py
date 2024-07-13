from django.urls import path
from tweet.views import PostingTweet, TweetAll, RetweetBase, LikeFeeds, SingleTweet, RetweetAll, LikeAll

urlpatterns = [
	path('posting',PostingTweet.as_view()),
	path('tweet',TweetAll.as_view()),
	path('tweet/<str:slug>',SingleTweet.as_view()),
	path('retweet/<int:num>',RetweetBase.as_view()),
	path('retweet',RetweetAll.as_view()),
	path('likes',LikeAll.as_view()),
	path('likes/<int:pk>/<int:author>',LikeFeeds.as_view()),
]