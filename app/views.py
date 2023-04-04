from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    tn=input("Enter the Topic_name: ")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse("This Is Insert_Topic")


def insert_Webpage(request):
    tn=input("Enter the topic_name: ")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input("Enter the Name:")
    u=input("Enter the url: ")
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    WO1=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO1.save()
    WO2=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO2.save()
    WO3=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO3.save()

    return HttpResponse("This Is Insert_Webpage")




def insert_accessmode(request):
    tn=input("Enter the topic_Name: ")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    w=input("Enter The Name: ")
    wu=input("Enter the URL: ")
    WO=Webpage.objects.get_or_create(topic_name=TO,name=w,url=wu)[0]
    WO.save()
    au=input("Enter the author: ")
    da=input("Enter the date: ")
    AC=Accessmode.objects.get_or_create(name=WO,author=au,date=da)[0]
    AC.save()
    AC1=Accessmode.objects.get_or_create(name=WO,author=au,date=da)[0]
    AC1.save()
    AC2=Accessmode.objects.get_or_create(name=WO,author=au,date=da)[0]
    AC2.save()


    return HttpResponse("This Is Insert_accessmode")






def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,"display_topic.html",d)


def display_webpage(request):
    LOT=Webpage.objects.all()
    d={'webpages':LOT}



    return render(request,"display_webpage.html",d)

def display_accessmode(request):
    LOT=Accessmode.objects.all()
    d={'accessmode':LOT}
    return render(request,"display_accessmode.html",d)