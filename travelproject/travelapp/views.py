from django.http import HttpResponse
from.models import place,team
from django.shortcuts import render


# Create your views here.

def demo(request):
    obj=place.objects.all()
    tm=team.objects.all()
    return render(request,'index.html',{'result':obj,'tm':tm})
