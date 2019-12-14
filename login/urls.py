from django.urls import path
from django.contrib.auth.models import User

from . import views

urlpatterns = [
	path(r'^(?P<User.id>[0-9]+)$', views.detail, name='detail'),
	path('', views.login_index, name='login_index'),
	path('register', views.register, name='register'),
	path('logout', views.user_logout, name='user_logout'),
]
