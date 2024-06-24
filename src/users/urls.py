from django.urls import path
from users.views import CreateUser,CekDokumen,LoginUsers,ProfileUsers, UpdateProfile,FollowUser

urlpatterns = [
	path('register',CreateUser.as_view()),
	path('login',LoginUsers.as_view()),
	path('dokumen/<str:id>',CekDokumen.as_view()),
	path('profile/<int:pk>',ProfileUsers.as_view()),
	path('profile/update/<int:pk>',UpdateProfile.as_view()),
	path('follow/<int:pk>',FollowUser.as_view()),
]