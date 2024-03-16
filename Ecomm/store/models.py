from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=30, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200,blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
# creat a user profile by default
def creat_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Automate the profile 
post_save.connect(creat_profile, sender=User)

# product Categories
class Category(models.Model):
    name =  models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class  Meta:
        verbose_name_plural = "categories"
    
# customers
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.last_name} {self.last_name}"
    
# products
class Product(models.Model):
    name = models.CharField(max_length=50)
    price= models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=50, default="", blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    on_sale = models.BooleanField(default= False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    def __str__(self):
        return f'{self.name} {self.price}'


# customers orders
class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50,default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.Product
