from django.db import models

# Create your models here.
class PastProject(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
    finishdate = models.DateField()


    def __str__(self):
         return self.name

class FutureProject(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
    finishdate = models.DateField()


    def __str__(self):
         return self.name

class Message(models.Model):
    namesurname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    bodytext= models.CharField(max_length=700)
    submitdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.namesurname
