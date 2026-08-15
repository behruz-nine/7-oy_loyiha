from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)])

    def __str__(self):
        return self.product_name