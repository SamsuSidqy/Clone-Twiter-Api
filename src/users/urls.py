from django.urls import path
from users.views import CreateUser,CekDokumen,LoginUsers

urlpatterns = [
	path('register',CreateUser.as_view()),
	path('login',LoginUsers.as_view()),
	path('dokumen/<str:id>',CekDokumen.as_view()),
]