from django.contrib.auth.models import User

from django import forms
#from django.contrib.auth.forms import UserChangeForm

from userprofile.models import UserProfile


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
		'username', 
		'first_name',
		'last_name',
		'email'
		]


class UpdateProfileForm(forms.ModelForm):
	image = forms.ImageField(label='Change Avatar',required=False, 
		error_messages = {'invalid':"Image files only"}, 
		widget=forms.FileInput()
		)

	class Meta:
		model = UserProfile
		fields = [
		'image',
		'description',
		'education',
		'graduated',
		'company',
		'still_work_here',
		'hometown',
		'current_city',
		'website',
		'gender',
		]

		labels = {
		'description': 'Bio',
		'education': 'School/College',
		'graduated': 'Graduated?',
		'company': 'Workplace/Company',
		'still_work_here': 'Still work here?',
		'hometown': 'Hometown',
		'current_city': 'Current City',
		'website': 'Website',
		}