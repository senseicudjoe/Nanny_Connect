from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import client,nurse
from authApp.models import Customuser



@receiver(post_save, sender=Customuser)
def create_nurse(sender, instance, created, **kwargs):
    if created:
        if instance.is_nurse == True:
            nurse_user = nurse()
            nurse_user.fname = '%s' % instance.first_name
            nurse_user.lname = '%s' % instance.last_name
            nurse_user.email = '%s' % instance.email
            nurse_user.save()

        elif instance.is_client == True:
            client_user = client()
            client_user.fname = '%s' % instance.first_name
            client_user.lname = '%s' % instance.last_name
            client_user.email = '%s' % instance.email
            client_user.save()
        else:
            pass

















       
