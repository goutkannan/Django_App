# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from geo.models import FlagData,GeoData


class FlagBotItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = FlagData


class CountryBotItem(DjangoItem):
    django_model = GeoData
    testfield = scrapy.Field()


