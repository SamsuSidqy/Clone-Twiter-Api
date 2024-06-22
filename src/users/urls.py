from django.urls import path
from users.views import CreateUser

urlpatterns = [
	path('register',CreateUser.as_view()),
]