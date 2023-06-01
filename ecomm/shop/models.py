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