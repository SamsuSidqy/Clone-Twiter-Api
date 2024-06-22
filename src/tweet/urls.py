from django.urls import path
from tweet.views import PostingTweet, TweetAll, RetweetAll, LikeFeeds, UnlikeFeeds

urlpatterns = [
	path('posting',PostingTweet.as_view()),
	path('tweet',TweetAll.as_view()),
	path('retweet/<int:num>',RetweetAll.as_view()),
	path('likes/<int:pk>/<int:author>',LikeFeeds.as_view()),
	path('unlikes/<int:pk>/<int:author>',UnlikeFeeds.as_view()),
]