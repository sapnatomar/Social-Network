from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
	path('login/', auth_views.LoginView.as_view(template_name= 'accounts/login.html'), name='login'),
	path('login_success/', views.login_success, name='login_success'),
	path('logout/', auth_views.LogoutView.as_view(template_name= 'accounts/logout.html'), name='logout'),
	path('register/', views.register, name='register'),

	#reset password urls
	path('resetpassword/', auth_views.PasswordResetView.as_view(), {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='password_reset'),
	path('resetpassword/done/', auth_views.PasswordResetDoneView.as_view(), {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
	path('resetpassword/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
	path('resetpassword/complete/', auth_views.PasswordResetCompleteView.as_view(), {'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'),
]