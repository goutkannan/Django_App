

from scrapy.spiders import BaseSpider
from flagbot.items import *


class flagSpider(BaseSpider):
    name="flagbot"
    allowed_domains = ["flagpedia.net"]
    start_urls= ["http://flagpedia.net/index"]

    def parse(self,response):
        td_country= response.xpath("//td[@class='td-country']/a/text() ").extract()
        td_flag = [ 'http:'+url.replace('h20','w580') for url in response.xpath("//td[@class='td-flag']/a/img/@src ").extract()]
        td_capital = response.xpath("//td[@class='td-capital']/text() ").extract()
        print(len(td_capital),len(td_flag),len(td_country))
#        return CountryBotItem(countryName='Italy',capitalName='Rome',currencyName='Euro')

        return CountryBotItem(countryName=td_country[0],capitalName=td_capital[0],currencyName='Euro')




        """
        countryBotItem["countryName"] = 'Newzeland'
        countryBotItem["currencyName"] = 'Dollar'
        countryBotItem["capitalName"] ='Wellington'
        countryBotItem.save()
"""




