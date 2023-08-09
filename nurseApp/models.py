from django.db import models
from authApp.models import Customuser
class nurse(models.Model):
    # user = models.ForeignKey(Customuser,on_delete=models.CASCADE,blank=True, null=True)
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    qualification = models.FileField(null=True, blank=True, upload_to="nurse_qualifications")
    DoB = models.DateField(blank=True, null=True) 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(blank = True, null = True,upload_to="nurse_images")
    day_shift = models.BooleanField(blank=True, null = True)
    night_shift = models.BooleanField(null=True, blank = True)
    bio = models.CharField(max_length = 300, blank=True, null = True)
    # reviews = 
    rate = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=2,null=True, blank=True)
    def __str__(self):
        return self.fname
# Create your models here.
