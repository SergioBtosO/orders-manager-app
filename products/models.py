from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=11)
    weight = models.DecimalField(decimal_places=2,max_digits=11)
    size = models.CharField(max_length=100)
    colors = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ' - ' + self.ref + ' - ' + self.name
