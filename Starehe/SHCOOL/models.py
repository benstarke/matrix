from django.db import models
from django.urls import reverse

# Create your models here.

class CAREER(models.Model):
    Title = models.CharField(max_length = 200)
    Photo = models.FileField(upload_to= 'photos')
    Description = models.TextField()
    
    def __str__ (self):
        return self.Title 


class Gallery(models.Model):
    Images = models.FileField(upload_to='gallery')

    # def __str__ (self):
    #     return self.Images


class Executive(models.Model):
    E_Photo = models.ImageField(upload_to = 'exec')
    E_Title = models.CharField(max_length=50)

class Services(models.Model):
    Service_Title = models.CharField(max_length=100)
    Service_Photo = models.FileField(upload_to= 'Services')
    Service_Description = models.TextField()

    def __str__ (self):
        return self.Service_Title