from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=222)

    def __str__(self):
        return self.city
    

class hotel(models.Model):
    name = models.CharField(max_length=222)
    date = models.DateField()
    ph =   models.PositiveIntegerField()
    city = models.ForeignKey(City,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
class add(models.Model):
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=222)
    food =models.CharField(max_length=222)
    wifi = models.CharField (max_length=222)
    water = models.CharField(max_length=222) 
    text  = models.CharField(max_length=200)
    image = CloudinaryField("image",null=True)

    def __int__(self):
        return self.id


class bookingss(models.Model):
     customer_name = models.CharField(max_length=100)
     room = models.ForeignKey(add, on_delete=models.CASCADE)
     check_in_date = models.DateField()
     check_out_date = models.DateField()



