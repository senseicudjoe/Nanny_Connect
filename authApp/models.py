from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customuser(AbstractUser):
     # extra fields which will be used when implementing the registration logic 
     is_nurse = models.BooleanField(default = False)
     is_client = models.BooleanField(default = False)
     is_admin = models.BooleanField(default = False)

     def __str__(self) -> str:
          return self.first_name