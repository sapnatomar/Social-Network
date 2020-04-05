from django.urls import path
from . import views

urlpatterns = [
	path('<pk>/full_post', views.view_post, name='view_post'),
	path('<pk>/edit/next?=<previous_page>/', views.edit_post, name='edit_post'),
	path('<pk>/edit/cancel/next?=<previous_page>/', views.cancel_post_activity, name='cancel_post_activity'),
	path('<pk>/delete/', views.delete_post, name='delete_post'),
	path('<pk>/<operation>/', views.like_unlike_post, name="like_unlike_post"),
]