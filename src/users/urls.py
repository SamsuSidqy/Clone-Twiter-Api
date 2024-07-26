from django.urls import path
from users.views import (CreateUser,LoginUsers,ProfileUsers, UpdateProfile,FollowUser,LogoutUsers,ListFollowers,
SearchingAcocunt)

urlpatterns = [
	path('register',CreateUser.as_view()),
	path('login',LoginUsers.as_view()),
	path('logout',LogoutUsers.as_view()),
	path('profile/<str:pk>',ProfileUsers.as_view()),
	path('profile/update/<int:pk>',UpdateProfile.as_view()),
	path('follow/<int:pk>',FollowUser.as_view()),
	path('search/<str:pk>',SearchingAcocunt.as_view()),
	path('follow/data',ListFollowers.as_view()),
]