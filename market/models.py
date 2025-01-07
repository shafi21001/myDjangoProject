from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=50)

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()
    supplier=models.CharField(max_length=255,default='supplier-1')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

    