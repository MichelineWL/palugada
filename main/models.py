import uuid 
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', default='default.jpg')

    @property
    def __str__(self):
        return self.name  # makes admin and shell outputs more readable
