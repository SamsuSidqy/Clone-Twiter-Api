from django.urls import path
from tweet.views import PostingTweet, TweetAll, RetweetAll

urlpatterns = [
	path('posting',PostingTweet.as_view()),
	path('tweet',TweetAll.as_view()),
	path('retweet/<int:num>',RetweetAll.as_view()),
]