from django.urls import path
from . import views

urlpatterns = [
	path('<id>/', views.comment_thread, name='comment_thread'),
	path('delete/<int:comment_id>/<int:reply_id>/', views.comment_delete, name='comment_delete'),
]