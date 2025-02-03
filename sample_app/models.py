from django.db import models

class AppModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(AppModel):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

class Product(AppModel):
    name = models.CharField(max_length=50)
    price = models.FloatField()

class Order(AppModel):
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_created']