from django.db import models
from nurseApp.models import nurse
class client(models.Model):
    fname=models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    picture = models.ImageField(blank = True, null = True, upload_to="client_images")
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
#     ratings = models.
    description = models.TextField()


    def __str__(self):
        return self.fname


class Request(models.Model):
    client = models.ForeignKey(client,on_delete=models.CASCADE)
    nurse = models.ForeignKey(nurse,on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()

    def __str__(self):
        return self.client.fname
# Create your models here.
