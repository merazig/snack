from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Pizza(models.Model):
    nom = models.CharField(max_length=255)
    prixm = models.DecimalField(max_digits=5, decimal_places=2)
    prixl = models.DecimalField(max_digits=5, decimal_places=2)
    descf = models.TextField()
    descb = models.TextField() 
    pimage = CloudinaryField('image')

class Burger(models.Model):
    nom = models.CharField(max_length=255)
    prixm = models.DecimalField(max_digits=5, decimal_places=2)
    prixl = models.DecimalField(max_digits=5, decimal_places=2)
    descf = models.TextField()
    descb = models.TextField() 
    bimage = CloudinaryField('image')
