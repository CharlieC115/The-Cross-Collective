from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    """ A model for maintaining users personal information and order history """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(max_length=16, null=True, blank=True)
    default_last_name = models.CharField(max_length=16, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_contact_number = models.CharField(max_length=16, null=True, blank=True)
    default_postcode = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update user profile information """

    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
