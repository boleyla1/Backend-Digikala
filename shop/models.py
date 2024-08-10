from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    Name = models.CharField(max_length=20)
    Image = models.ImageField(upload_to='images/',default='default.jpg')

    def __str__(self):
        return self.Name


class Customer(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.FirstName


class Product(models.Model):
    Name = models.CharField(max_length=20)
    discription = models.CharField(max_length=200, default='', blank=True, null=True)
    Price = models.IntegerField(default=0)
    Category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    Pictur = models.ImageField(upload_to='upload/products/')
    Star = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(5)))
    Offer = models.BooleanField(default=False)
    OfferPrice = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Adress = models.CharField(max_length=200, blank=False)
    Phone = models.CharField(max_length=20, blank=True)
    Date = models.DateField(default=datetime.date.today)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Product
