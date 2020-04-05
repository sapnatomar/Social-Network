from django.contrib.auth.models import User

from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
import random

from friendship.models import Friend, Follow, Block
from posts.models import Post
from posts.forms import PostForm


class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self, request):
		current_page = 'home'
		form = PostForm(auto_id=False)
		posts_list = Post.objects.all().order_by('-created')

		me = request.user.userprofile

		paginator = Paginator(posts_list,10)
		page = request.GET.get('page')
		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
			posts = paginator.page(1)
		except EmptyPage:
			posts = paginator.page(paginator.num_pages)

		users = User.objects.exclude(id=request.user.id)
		users_count = users.count()

		args = {
			'form': form, 
			'posts': posts, 
			'users': users,  
			'current_page':current_page,
			'me': me,
			}
		return render(request, self.template_name, args)



	def post(self, request):
		current_page = 'home'
		form = PostForm(request.POST, request.FILES or None, auto_id=False)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			messages.success(request, "Post successfully created!")
			text = form.cleaned_data['post']
		else:
			messages.error(request, "Post not created!")

		form = PostForm()
		return redirect('home:home')

		args = {'form': form, 
			'text': text,  
			'current_page':current_page,
			}
		return render(request, self.template_name, args)

		

def search_user(request):
	user_name = request.GET.get('username')
	users_list = User.objects.all()
	users = []
	users_count = 0
	
	if user_name:
		users = users_list.filter(username__icontains=user_name) | users_list.filter(first_name__icontains=user_name, last_name__icontains=user_name) | users_list.filter(first_name__icontains=user_name) | users_list.filter(last_name__icontains=user_name)
		users_count = users.count()

	
	args = {
		'current_page': 'search_user',
		'users': users, 
		'users_count': users_count, 
		'user_name':user_name,
		'me': request.user.userprofile,
		}
	return render(request, 'home/search_user.html', args)
	