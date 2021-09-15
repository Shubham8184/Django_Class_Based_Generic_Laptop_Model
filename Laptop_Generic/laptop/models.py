from django.db import models



class LaptopModel(models.Model):
    laptopname=models.CharField(max_length=30)
    laptopCompany=models.CharField(max_length=30)
    laptopram=models.IntegerField()
    laptoprom=models.IntegerField()
    laptopprice=models.IntegerField()
    laptopprocessor=models.CharField(max_length=30)

    def __str__(self):
        return self.laptopname
