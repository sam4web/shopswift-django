import uuid

from django.contrib.auth.models import User
from django.db import models

CATEGORIES = (
    (
        1,
        "Apparels & Accessories",
    ),
    (
        2,
        "Automobiles",
    ),
    (
        3,
        "Beauty & Health",
    ),
    (
        4,
        "Books & Learning",
    ),
    (
        5,
        "Business & Industrial",
    ),
    (
        6,
        "Computers & Peripherals",
    ),
    (
        7,
        "Electronics, TVs & More",
    ),
    (
        8,
        "Events & Happenings",
    ),
    (
        9,
        "Fresh Veggies & Meat",
    ),
    (
        10,
        "Furnishings & Appliances",
    ),
    (
        11,
        "Jobs",
    ),
    (
        12,
        "Mobile Phone & Accessories",
    ),
    (
        13,
        "Music Instruments",
    ),
    (
        14,
        "Pets & Adoption & Free Stuff",
    ),
    (
        15,
        "Real Estate",
    ),
    (
        16,
        "Services",
    ),
    (
        17,
        "Sports & Fitness",
    ),
    (
        18,
        "Toys & Video Games",
    ),
    (
        19,
        "Travel, Tours & Packages",
    ),
)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    category = models.IntegerField(choices=CATEGORIES)
    image = models.ImageField(upload_to="product/")
    created_by = models.ForeignKey(
        User, related_name="products", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
