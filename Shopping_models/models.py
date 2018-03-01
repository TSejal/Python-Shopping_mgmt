from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    email = models.EmailField('email address', unique = True)
    first_name = models.CharField('first name', max_length = 255, blank = True)
    last_name = models.CharField('last name', max_length = 255, blank = True)
    avatar = models.ImageField(upload_to = 'avatar/')
    country = models.CharField(max_length = 255, verbose_name = 'Country')
    is_active = models.BooleanField('active', default = True)
    date_joined = models.DateTimeField('date joined',default = timezone.now)

    def __str__(self):
        return self.first_name

class Seller(models.Model):
    profile = models.OneToOneField(User, related_name = "user_seller_profile")
    store_name = models.CharField(max_length = 255, null = True, blank = True)
    website = models.URLField('Store Website', null = True, blank = True)
    enabled = models.BooleanField(default = False)
    date_added = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.store_name


class Product(models.Model):
    title = models.CharField(max_length = 255, null = True, blank = True)
    category = models.CharField(max_length = 50, null = True, blank = True)
    quantity = models.PositiveIntegerField(null = True, blank = True)
    unit_sold = models.PositiveIntegerField(null = True, blank = True, default = 0)
    price = models.DecimalField(max_digits = 16, decimal_places = 2)
    added_by = models.ForeignKey(User, related_name = 'added_products')
    publish_status = models.BooleanField(default = False)
    date_added = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.title
