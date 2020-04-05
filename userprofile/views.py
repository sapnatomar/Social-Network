from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
#from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, Http404

from userprofile.forms import UserUpdateForm, UpdateProfileForm

from posts.models import Post
from friendship.models import Friend, Follow, Block, FriendshipRequest

# Create your views here.

def view_profile(request, pk=None):
	current_page = 'profile'

	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user

	me = request.user.userprofile

	if request.user in user.userprofile.blocks or user in me.blocks:
		reponse = HttpResponse("Permission denied.")
		reponse.status_code = 403
		return reponse

	posts = Post.objects.filter(user=user).order_by('-created')
	
	args = {'user': user,
		'posts': posts,
		'current_page':current_page,
		'me': me,
		}
	return render(request, 'userprofile/profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = UpdateProfileForm(request.POST,
								request.FILES,
								instance=request.user.userprofile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, "Profile successfully updated!")
		else:
			messages.error(request, "Profile not updated. Enter valid data!")
		return redirect('userprofile:edit_profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = UpdateProfileForm(instance=request.user.userprofile)

	args = {'u_form': u_form, 'p_form': p_form}
	return render(request, 'userprofile/edit_profile.html', args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, "Password successfully changed!")
			return redirect('home:home')
		else:
			messages.error(request, "Password not changed. Enter a valid password")
			return redirect('userprofile:change_password')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form, }
		return render(request, 'userprofile/change_password.html', args)
