from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
import json


def cekserver(req):
    return HttpResponse(json.dumps({"status":200}),content_type="application/json")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('users.urls')),
    path('api/users/v1/',include('tweet.urls')),    
    path('cekserver',cekserver),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)