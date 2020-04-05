from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date
from friendship.models import Friend, Block

# Create your models here.
class UserProfileManager(models.Manager):
	def get_queryset(self):
		return super(UserProfileManager, self).get_queryset().filter(city='Kanpur')

def upload_location(instance, filename):
	return "profile_images/%s/%s" % (instance.user, filename)

class UserProfile(models.Model):
	gender_choices = (
			('Male', 'Male'),
			('Female', 'Female'),
			('Custom', 'Custom')
			)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=150, default='Exploring World!', null=True, blank=True)
	education = models.CharField(max_length=50, default='', null=True, blank=True)
	graduated = models.NullBooleanField(default=True)
	company = models.CharField(max_length=50, default='', null=True, blank=True)
	still_work_here = models.NullBooleanField()
	hometown = models.CharField(max_length=30, default='', null=True, blank=True)
	current_city = models.CharField(max_length=30, default='', null=True, blank=True)
	image = models.ImageField(default='profile_images/default.jpg',upload_to=upload_location,null=True, blank=True)
	website = models.URLField(default='', blank=True, null=True)
	gender = models.CharField(max_length=10, choices=gender_choices, null=True, blank=True)
	has_previously_logged_in = models.BooleanField(default=False)


	#kanpur = UserProfileManager()

	def __str__(self):
		return self.user.username

	@property
	def profilepic_or_default(self, default_path="profile_images/default.jpg"):
		if self.image:
			return self.image
		return default_path

	@property
	def friends(self):
		instance = self.user
		qs = Friend.objects.friends(instance)
		return qs

	@property
	def friends_count(self):
		instance = self.friends
		return len(instance)

	@property
	def friend_requests(self):
		qs = Friend.objects.unrejected_requests(user=self.user)
		return [q.from_user for q in qs]

	@property
	def fr_count(self):
		instance = self.friend_requests
		return len(instance)
		
	@property
	def sent_requests(self):
		qs = Friend.objects.sent_requests(user=self.user)
		return [q.to_user for q in qs]

	@property
	def sr_count(self):
		instance = self.sent_requests
		return len(instance)

	@property
	def blocks(self):
		instance = self.user
		qs = Block.objects.blocking(instance)
		return qs

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
