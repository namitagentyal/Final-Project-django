from django.db import models

# # Create your models here.
class Bestsellers(models.Model):

    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='bestsellers', default='NA')
   
class Bestsellers_combos(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='bestsellers_combos', default='NA')

class New_Launches(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='new_launches', default='NA')

class Moisturize(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='moisturize', default='NA')

class AllProducts(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='allproducts', default='NA')