

# Create your models here.
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200)
    address = models.TextField()
    property_type = models.CharField(max_length=50)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/')
    more_images = models.ImageField(upload_to='property_images/', blank=True, null=True)

    def __str__(self):
        return self.title
