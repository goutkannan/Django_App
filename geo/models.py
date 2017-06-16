from django.db import models

# Create your models here.
class GeoData(models.Model):
    countryName = models.CharField(max_length=100)
    capitalName = models.CharField(max_length=100)
    currencyName = models.CharField(max_length=100)

    def __str__(self):
        return  self.countryName+"'s capital is "+self.capitalName


class FlagData(models.Model):
    country = models.ForeignKey(GeoData, on_delete=models.CASCADE)
    flagURL = models.CharField(max_length=500)

    def __str__(self):
        return self.country.countryName+"'s flag is added"



