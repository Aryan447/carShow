from django.db import models

# Create your models here.

class Contact(models.Model):
    Fname = models.TextField()
    Lname = models.TextField()
    Email = models.TextField()
    Queries = models.TextField()

class Gallery(models.Model):
    carName = models.TextField()
    carImage = models.ImageField(upload_to='myapp/static/images/')