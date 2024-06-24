from django.contrib import admin
from users.models import Users
from rest_framework.authtoken.models import Token
# Register your models here.


admin.site.register(Users)
