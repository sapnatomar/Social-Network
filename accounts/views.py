from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404

from accounts.forms import RegistrationForm

# Create your views here.

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, "%s successfully registered!" % username)
			return redirect('home:home')
		else:
			messages.error(request, "Enter a valid email address! Make sure to enter same password in both password fields. If user still not registered, try using a different username.")
			return redirect('accounts:register')
	else:
		form = RegistrationForm()
		args = {'form': form}
		return render(request, 'accounts/register.html', args)

def login_success(request):
	user = request.user
	if not user.userprofile.has_previously_logged_in:
		user.userprofile.has_previously_logged_in = True
		user.userprofile.save()
		return redirect('userprofile:edit_profile')
	else:
		return redirect('home:home')
