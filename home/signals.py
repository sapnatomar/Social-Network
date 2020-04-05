from django.db.models.signals import post_save
from django.contrib.auth.models import User
from home.models import Friend
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_Friend_list(sender, instance, created, **kwargs):
	if created:
		Friend.objects.create(current_user=instance)

@receiver(post_save, sender=User)
def save_Friend_list(sender, instance, **kwargs):
	instance.user.save()