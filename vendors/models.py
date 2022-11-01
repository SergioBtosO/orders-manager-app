from django.db import models

# Create your models here.
class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    document = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} | {self.document} | {self.name}'

