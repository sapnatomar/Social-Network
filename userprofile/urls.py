from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
	path('', views.view_profile, name='view_profile'),
	path('view/<pk>/', views.view_profile, name='view_profile_with_pk'),
	path('update/', views.edit_profile, name='edit_profile'),
	path('user/changepassword/', views.change_password, name='change_password'),
	]