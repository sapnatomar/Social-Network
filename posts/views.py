from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.views.generic import TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages

from friendship.models import Friend, Follow, Block
from posts.forms import PostForm, EditPostForm
from posts.models import *

from comments.models import Comment
from comments.forms import CommentForm


def view_post(request, pk):
	current_page = 'view-post'
	try:
		post = Post.objects.get(pk=pk)
	except:
		raise Http404

	if not (request.user == post.user or request.user in Friend.objects.friends(post.user)) or request.user in Block.objects.blocking(post.user):
		reponse = HttpResponse("Permission denied.")
		reponse.status_code = 403
		return reponse

	initial_data = {
		'content_type': post.get_content_type,
		'object_id': post.id,
	}

	comment_form = CommentForm(request.POST or None, initial=initial_data)
	if comment_form.is_valid():
		c_type = comment_form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = comment_form.cleaned_data.get("object_id")
		content_data = comment_form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()

		new_comment, created = Comment.objects.get_or_create(
										user=request.user,
										content_type=content_type,
										object_id=obj_id,
										content=content_data,
										parent=parent_obj,
										)
		return redirect("posts:view_post",pk=pk)

	comments = Comment.objects.filter_by_instance(post)

	args = {'post': post, 
		'comments':comments,
		'current_page': current_page,
		'comment_form': comment_form,
		'me': request.user.userprofile,
		}
	return render(request, 'posts/view_post.html', args)


def delete_post(request, pk, previous_page=None):
	try:
		post = Post.objects.get(pk=pk)
	except:
		raise Http404

	if post.user != request.user:
		reponse = HttpResponse("Permission denied.")
		reponse.status_code = 403
		return reponse

	post.delete()
	messages.success(request, "Post successfully deleted!")
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def edit_post(request, pk, previous_page=None):
	try:
		post = Post.objects.get(pk=pk)
	except:
		raise Http404

	if post.user != request.user:
		reponse = HttpResponse("Permission denied.")
		reponse.status_code = 403
		return reponse

	if request.method == 'POST':
		form = EditPostForm(request.POST, request.FILES, instance=post, auto_id=False)
		if form.is_valid():
			post.save()
			messages.success(request, "Post successfully updated!")
			return redirect('posts:view_post', pk=pk)
	else:
		form = EditPostForm(instance=post, auto_id=False)
		args = {'form': form, 
			'post': post, 
			'previous_page':previous_page
			}
		return render(request, 'posts/edit_post.html', args)


def cancel_post_activity(request, pk, previous_page=None):
	if previous_page == 'profile':
		return redirect('userprofile:view_profile')
	elif previous_page == 'view-post':
		return redirect('posts:view_post', pk=pk)
	else:
		return redirect('home:home')

def like_unlike_post(request, pk, operation):
	try:
		post = Post.objects.get(pk=pk)
	except:
		raise Http404

	if not (request.user == post.user or request.user in post.user.userprofile.friends):
		reponse = HttpResponse("Permission denied.")
		reponse.status_code = 403
		return reponse

	if operation == 'unlike':
		post.remove_like(request.user)
	elif operation =='like':
		post.add_like(request.user)

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))