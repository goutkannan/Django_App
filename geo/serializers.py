from rest_framework import serializers
from .models import GeoData,FlagData

class GeoSerializer(serializers.ModelSerializer ):
    class  Meta:
        model = GeoData
        fields = ('id','countryName','capitalName','currencyName')

class flagSerializer(serializers.ModelSerializer):
    country= GeoSerializer()
    class Meta:
        model = FlagData
        fields= ('country','flagURL')
