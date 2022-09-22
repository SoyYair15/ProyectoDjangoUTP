from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		userprofile = UserProfile.objects.create(user=instance)

#APARTADO QUE USA LAS SEÑALES OFICIALES DE DJANGO, EN ESTE CASO SE USA EL POST_SAVE