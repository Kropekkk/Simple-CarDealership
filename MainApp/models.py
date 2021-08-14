from django.db import models

class Offer(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    generation = models.CharField(max_length=8,blank=True)
    year = models.CharField(max_length=4)
    distance = models.CharField(max_length=7)
    price=models.CharField(max_length=7)
    mainimage = models.ImageField(upload_to='images')
    description=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.brand} {self.model}"