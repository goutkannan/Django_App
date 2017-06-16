# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from geo.models import flags,Geo


class FlagBotItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = flags

class CountryBotItem(DjangoItem):
    django_model = Geo


