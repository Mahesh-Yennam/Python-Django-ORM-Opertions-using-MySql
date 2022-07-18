from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    contact=models.IntegerField(default=0)
    password=models.CharField(max_length=15)
    description=models.TextField(max_length=200)

    class Meta:
        db_table='emp'

    def __str__(self):
        return self.name

class Account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=20)
    description=models.TextField(max_length=200)
    emp=models.ForeignKey(Emp, on_delete=models.CASCADE)
    class Meta:
        db_table='account'
    