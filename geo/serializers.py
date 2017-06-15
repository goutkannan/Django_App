from rest_framework import serializers
from .models import Geo,flags

class GeoSerializer(serializers.ModelSerializer ):
    class  Meta:
        model = Geo
        fields = ('id','countryName','capitalName','currencyName')

class flagSerializer(serializers.ModelSerializer):
    country= GeoSerializer()
    class Meta:
        model = flags
        fields= ('country','flagURL')
