from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.CharField(max_length=200)
    image = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'Category : {self.category} : {self.title}'
    
    class Meta:
        ordering = ['image', 'category', 'title',
                    'description', 'price', 'discounted_price']

class Order(models.Model):
    print("Got into models. py and trying to save the world")
    items = models.CharField(max_length=1000)
    print(f"Got into models. py and trying to save the world : {items}")
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    totalPrice = models.CharField(max_length=200)

    class Meta:
        ordering = [
            "name", "email", "address", "city", "zipcode", "state", "items", "totalPrice"
        ]