from django import forms
from django.forms import ModelForm
from posts.models import Post

class PostForm(ModelForm):
	post = forms.CharField(widget=forms.Textarea(
			attrs = {
				'class':'form-control custom-textarea',
				'placeholder':'Write a post...',
				'rows':4,
			}
		))

	post_image = forms.ImageField(label='Image',required=False, 
			error_messages = {'invalid':"Image files only"}, 
			widget=forms.FileInput()
			)

	class Meta:
		model = Post
		fields = ['post', 'post_image']

class EditPostForm(ModelForm):
	post = forms.CharField(widget=forms.Textarea(
			attrs = {
				'class':'form-control',
				'rows':8,
			}
		))
	post_image = forms.ImageField(label='Image',required=False, 
			error_messages = {'invalid':"Image files only"}, 
			widget=forms.FileInput()
			)

	class Meta:
		model = Post
		fields = ['post','post_image']

		