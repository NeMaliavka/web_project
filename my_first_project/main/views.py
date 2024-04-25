from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h4> проверка работы </h4>') #itproger
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')
    #return HttpResponse('<h4> Страница про нас </h4>') #itproger

def crm(request):
    return HttpResponse('<h4> Тут будут данные </h4>') #itproger
