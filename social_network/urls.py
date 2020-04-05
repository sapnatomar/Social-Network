"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from social_network import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500,handler403, handler400


urlpatterns = [
	path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('profile/', include(('userprofile.urls', 'userprofile'), namespace='userprofile')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('comments/', include(('comments.urls', 'comments'), namespace='comments')),
    path('friends/', include(('friends.urls', 'friends'), namespace='friends')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
