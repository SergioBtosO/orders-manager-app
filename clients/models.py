from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    nit = models.IntegerField()
    address = models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.nit + ' - ' + self.name
