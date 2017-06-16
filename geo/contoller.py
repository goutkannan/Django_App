from bs4 import BeautifulSoup
import requests
from geo.models import FlagData, GeoData


def loadGeoData():
    data = requests.get("http://flagpedia.net/index").text
    dataSoup = BeautifulSoup(data)
    flag_URL_list=[]
    country_list=[]
    currency_list = []
    capital_list=[]

    for row in dataSoup.find_all('td',attrs="td-flag"):
        flag_URL_list.append('http:'+row.find('img')['src'].replace('h20','w580'))

    for row in dataSoup.find_all('td',attrs="td-country"):
        country_list.append(row.find('a').text)
    for row in dataSoup.find_all('td',attrs="td-capital"):
        capital_list.append(row.text)

    currency_data = requests.get("https://www.spotthelost.com/country-capital-currency.php").content
    csoup = BeautifulSoup(currency_data)
    print('trying...')

    selector = "tr > td"
    row= (csoup.select(selector=selector)[1:])

    currency_dict ={}

    for i in range(0, len(row), 3):
        print(" country Name: ", row[i].text)
        if(row[i].text.strip() == 'Bangladesh'):
            print(row[i + 2].text)
        currency_dict[row[i].text.strip()] = row[i + 2].text


    for i in range(len(country_list)):
        g = GeoData()
        f = FlagData()



        if (country_list[i]):
            
                g.countryName = country_list[i]
                print(" capital : ", capital_list[i])
                g.capitalName = capital_list[i]
                curr = currency_dict[country_list[i]] if country_list[i].strip() in currency_dict.keys() else "N/A"
                print(" currecy :", curr)
                g.currencyName = curr
                print(" >>URL: ", flag_URL_list[i])
                g.save()
                if(g is not None):
                    f.country = g

                    f.flagURL = flag_URL_list[i]
                    f.save()
        else:
            print("None ")




