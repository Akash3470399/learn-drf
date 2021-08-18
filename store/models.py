from django.db import models

# Create your models here.
class Store(models.Model):
    user_id = models.PositiveIntegerField(unique=True)
    banner = models.ImageField(upload_to='banners/',blank=True, default='/banners/default.png')
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, default="profile/default.png")
    store_name = models.CharField(max_length=250)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length =100)
    state = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()