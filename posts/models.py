from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify

from comments.models import Comment

# Create your models here.
def upload_location(instance, filename):
	return "post_images/%s/%s" % (instance.user, filename)

class Post(models.Model):
	post = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	#slug = models.SlugField(unique=True)
	post_image = models.ImageField(upload_to=upload_location, null=True, blank=True, 
		height_field="height_field", 
		width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	likes = models.ManyToManyField(User, related_name="likes", blank=True)

	post_obj = GenericRelation(Comment, object_id_field="object_id", related_query_name="post")

	def __str__(self):
		return str(self.user) + ' wrote... ' + str(self.post)

	def add_like(self, liker):
		self.likes.add(liker)

	def remove_like(self, unliker):
		self.likes.remove(unliker)

	@property
	def count_likes(self):
		return self.likes.count()

	@property
	def post_word_count(self):
		text = self.post
		count = len(text.split())
		return count

	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(instance)
		return qs

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type

