from django.urls import path
from . import views

urlpatterns = [
	path('send-request/<id>/', views.send_friend_request, name='send-request'),
	path('cancel-request/<id>/', views.cancel_friend_request, name='cancel-request'),
	path('accept-request/<id>/', views.accept_friend_request, name='accept-request'),
	path('reject-request/<id>/', views.reject_friend_request, name='reject-request'),
	path('remove-friend/<id>/', views.remove_friend, name='remove-friend'),
	path('block-user/<id>/', views.block_user, name='block_user'),
	path('unblock-user/<id>/', views.unblock_user, name='unblock_user'),
]