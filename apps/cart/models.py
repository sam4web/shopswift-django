import uuid

from django.contrib.auth.models import User
from django.db import models

from apps.product.models import Product


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, related_name="carts", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.username}'s Cart"

    def get_total(self):
        return sum(product.price for product in self.products.all())


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def cost(self):
        return sum(product.price for product in self.products.all())

    def __str__(self):
        return f"{self.name}'s orders ({self.created_at})"
