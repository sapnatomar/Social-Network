from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs = {'placeholder':'First Name',}))
	last_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs = {'placeholder':'Last Name',}))
	email = forms.EmailField(required=True, label="", widget=forms.EmailInput(attrs = {'placeholder':'Email',}))
	username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
	password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password Confirm'}))

	class Meta:
		model = User
		fields = {
		'username',
		'first_name',
		'last_name',
		'email',
		'password1',
		'password2',
		}

		def save(self, commit=True):
			user = super(RegistrationForm, self).save(commit=False)
			user.first_name = self.cleaned_data['first_name']
			user.last_name = self.cleaned_data['last_name']
			user.email = self.cleaned_data['email']

			if commit:
				user.save()

			return user