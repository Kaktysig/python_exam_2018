from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Customer(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Category(models.Model):

    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.name


class Good(models.Model):

    name = models.CharField(max_length=140)

    category = models.ForeignKey('Category', related_name='goods')

    def __str__(self):
        return self.name

class Goods_Variation(models.Model):

    parent = models.ForeignKey('Good', related_name="good")

    variation_name = models.CharField(max_length=140)
    description = models.TextField(blank=True)

    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.parent.name + " " + self.variation_name

    def category(self):
        return self.parent.name


class Cart(models.Model):

    customer = models.ForeignKey(Customer, related_name="cart", blank=True, default=None, null=True)

    goods = models.ManyToManyField('Goods_Variation', related_name="in_cart")

    def customer_name(self):
        return self.customer.username

    def customer_email(self):
        return self.customer.email


class Order(models.Model):

    customer = models.ForeignKey(Customer, related_name="order")

    address = models.CharField(max_length=150)
    datetime = models.DateField()

    goods = models.ForeignKey('Cart', related_name="ordered")