from django.test import TestCase
# from django.db import models

# class admin_1(models.Model):
#     fname = models.CharField(max_length=60)
#     lname = models.CharField(max_length=60)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=20)
#     image = models.ImageField(upload_to="admin_images")

#     def __str__(self):
#         return self.fname
    
# class company(models.Model):
#     name = models.CharField(max_length=60)
#     logo = models.ImageField(upload_to="logo")
#     location = models.CharField(max_length=100)
#     about_us = models.TextField()
#     admin = models.ForeignKey(admin_1,on_delete=models.CASCADE)
#     nurse = models.ManyToManyField(nurse)

#     def __str__(self):
#         return self.name
# Create your tests here.
