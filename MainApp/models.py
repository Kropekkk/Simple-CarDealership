from django.db import models

BRAND_CHOICES = (
    ('TESLA','TESLA'),
    ('SUZUKI','SUZUKI'),
)

MODEL_CHOICES = (

)

class Car(models.Model):
    brand = models.CharField(choices=BRAND_CHOICES,max_length=20)
    model = models.CharField(max_length=20)
    year_production = models.IntegerField()

class Details(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)