from django.db import models

# Create your models here.

class Product(models.Model):
    firstname = models.CharField( max_length=50)
    lastname = models.CharField(  max_length=50)
    
    def __str__(self):
        return self.firstname + " " + self.lastname
    
    
class Img(models.Model):
    imageName = models.CharField(max_length=200)
    imageDesc = models.TextField()
    imageTime = models.DateTimeField(auto_now_add=True)
    imageFile = models.ImageField(upload_to='upload_images/')
    
    def __str__(self):
        return self.imageName
    