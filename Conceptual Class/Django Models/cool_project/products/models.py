from django.db import models
from uuid import uuid4

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    description = models.TextField()
    is_sold = models.BooleanField(default=False)

    uuid = models.UUIDField(default=uuid4, primary_key=True)

    def __str__(self):
        return self.name


# python manage.py shell (to experiment)

# from products.models import Product

# Product.objects.create(name='Pen', price=5, description="A nice pen.")

# my_product = Product.objects.get(id=1) [it will always return 1 object]
# my_product.price

# my_product = Product.objects.filter(name='pen') [it can return multiple object]
# my_product[0].price
# for product in my_product:
#     print(product.name, product.price, product.description, product.is_sold)

