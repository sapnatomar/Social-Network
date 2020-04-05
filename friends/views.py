from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages

from friendship.models import Friend, Follow, Block, FriendshipRequest

# Create your views here.

def send_friend_request(request, id):
	try:
		other_user = User.objects.get(id=id)
	except:
		raise Http404
	Friend.objects.add_friend(request.user, other_user)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cancel_friend_request(request, id):
	try:
		user = User.objects.get(id=id)
	except:
		raise Http404
	sfr = FriendshipRequest.objects.get(from_user=request.user, to_user=user)
	f_request = get_object_or_404(request.user.friendship_requests_sent, id=sfr.id)
	to_user = f_request.to_user.pk
	f_request.cancel()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def accept_friend_request(request, id):
	try:
		user = User.objects.get(id=id)
	except:
		raise Http404
	fr = FriendshipRequest.objects.get(from_user=user, to_user=request.user)
	f_request = get_object_or_404(request.user.friendship_requests_received, id=fr.id)
	from_user = f_request.from_user.pk
	f_request.accept()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def reject_friend_request(request, id):
	try:
		user = User.objects.get(id=id)
	except:
		raise Http404
	fr = FriendshipRequest.objects.get(from_user=user, to_user=request.user)
	f_request = get_object_or_404(request.user.friendship_requests_received, id=fr.id)
	from_user = f_request.from_user.pk
	f_request.reject()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_friend(request, id):
	try:
		other_user = User.objects.get(id=id)
	except:
		raise Http404
	Friend.objects.remove_friend(request.user, other_user)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def block_user(request, id):
	try:
		user = User.objects.get(id=id)
	except:
		raise Http404
	if Friend.objects.are_friends(user, request.user):
		Friend.objects.remove_friend(request.user, user)
	elif not Friend.objects.can_request_send(user, request.user):
		sfr = FriendshipRequest.objects.get(from_user=request.user, to_user=user)
		f_request = get_object_or_404(request.user.friendship_requests_sent, id=sfr.id)
		f_request.cancel()
	elif not Friend.objects.can_request_send(reqest.user, user):
		fr = FriendshipRequest.objects.get(from_user=user, to_user=request.user)
		f_request = get_object_or_404(request.user.friendship_requests_sent, id=fr.id)
		f_request.cancel()
		
	Block.objects.add_block(request.user, user)
	return redirect("home:home")

def unblock_user(request, id):
	try:
		other_user = User.objects.get(id=id)
	except:
		raise Http404
	Block.objects.remove_block(request.user, other_user)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))