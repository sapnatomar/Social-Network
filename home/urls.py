from django.urls import path
from home.views import HomeView
from . import views

urlpatterns = [
	path('home/', HomeView.as_view(), name='home'),
	path('search_user', views.search_user, name='search_user'),
]