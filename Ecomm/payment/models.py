from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShippingAdress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=200)
    shipping_email = models.CharField(max_length=200)
    shipping_address1  = models.CharField(max_length=200)
    shipping_address2 = models.CharField(max_length =200, null=True, blank=True)
    shipping_city = models.CharField(max_length=200)
    shipping_country = models.CharField(max_length=200,)
    shipping_state = models.CharField(max_length=200, null=True, blank=True)
    shipping_zip = models.CharField(max_length=200, null=True, blank=True)

    # dont make address plural
    class Meta:
        verbose_name_plural = "shipping Address"
    
    def __str__(self):
        return f'Shipping Address - {str(self.id)}'