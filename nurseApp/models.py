from django.db import models

class nurse(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    qualification = models.FileField(null=True, blank=True, upload_to="nurse_qualifications")
    DoB = models.DateField() 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    image = models.ImageField(blank = True, null = True,upload_to="nurse_images")
    start_work = models.DateTimeField()
    end_work = models.DateTimeField()
    # bio = models.CharField(max_length = 300, blank=True, null = True)
    def __str__(self):
        return self.fname
# Create your models here.
