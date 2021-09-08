from django.db import models

# Create your models here.
from apps.product.models import Product
from apps.vendor.models import Vendor

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    vendors = models.ManyToManyField(Vendor, related_name='orders')

    class Meta:
        ordering = ['-created_at']
        #( make order date always to top of list )
    
    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='items', on_delete=models.CASCADE)
    vendor_paid = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return '%s' % self.id
    
    def get_total_price(self):
        return self.price * self.quantity