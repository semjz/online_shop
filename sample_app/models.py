from django.core.validators import MinValueValidator
from django.db import models
from authentication.models import User

class AppModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(AppModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

class Product(AppModel):
    name = models.CharField(max_length=50)
    price = models.FloatField(validators=[MinValueValidator(0.0)])

class Order(AppModel):
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['date_created']