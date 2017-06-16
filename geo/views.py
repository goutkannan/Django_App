import random

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from .models import GeoData,FlagData
from .serializers import GeoSerializer,flagSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

class randques(object):
    qno = random.sample(range(1,16),15)
    count =0
    @classmethod
    def get(cls):
        if cls.count <14:
            cls.count += 1
        else:
            cls.count = 0
        print(".."+str(cls.count))
        print("..."+str(cls.qno[cls.count]))
        return cls.qno[cls.count]




# Create your views here.
@api_view(['GET'])
def list(request):
    geoData = GeoData.objects.all()
    serialize = GeoSerializer(geoData,many=True)
    return Response(serialize.data)

@api_view(['GET'])
def listflag(request):
    flagData = flagData.objects.all()
    serialize = flagSerializer(flagData,many=True)
    return Response(serialize.data)


def index(request):
    return HttpResponse("<h1> Test your geographic knowledge</h1>"
                        "<p> What do you know ?</p>")

def home(request):
    """Renders the home page."""
    context =  GeoData.objects.all()

    assert isinstance(request, HttpRequest)
    return render(request,'app/index.html',{'context':context} )

def contact(request):
    """Renders the contact page."""
    context =  {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
                }
    assert isinstance(request, HttpRequest)
    return render(request,'app/contact.html',context )


score=0
country=""

@api_view(['GET','POST'])

def about(request):
    """Renders the about page."""

    msg=""
    global  score,country

    if request.method == 'POST':
        for key,value in request.POST.items():
            msg = country
            print(key,value)
            if value ==country:
                msg = value
                score+=1

        if score == 10:
            context = {'score': score,
                   'message': 'Congrats'
                }
            score = 0
            return render(request, 'app/a_template.html', context)


    random.seed()
    #indx = random.randint(1, 12)
    indx = randques.get()
    print(indx)
    url = FlagData.objects.get(pk=indx).flagURL
    country = FlagData.objects.get(pk=indx).country.countryName
    options = [country]
    optioncount =3
    while optioncount!=0:
        optionCountry = FlagData.objects.get(pk=random.randint(1, 12)).country.countryName

        if optionCountry not in options:
            options.append(optionCountry)
            optioncount-=1
    random.shuffle(options)

    #assert isinstance(request, HttpRequest)

    s = score
    context ={
            'title':msg ,
            'message':'Guess the countries..!!',
            'flag':url,
            'countryOption' : options,

            'score' : s
        }
    return render(request, 'app/ques.html', context)

