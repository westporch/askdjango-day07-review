from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'), # 예) http://192.168.0.7:8080/accounts/login/
]
