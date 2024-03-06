from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.http import  HttpResponse


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request, 'about.html', {'next_page_url': reverse('page1')})


def page1(request):
    return render(request,'page1.html',{'previous_page_url': reverse('about'),'next_page_url': reverse('page2')})

def page2(request):
    return render(request, 'page2.html', {'previous_page_url': reverse('page1'), 'next_page_url': reverse('page3')})


def page3(request):
    return render(request, 'page3.html', {'previous_page_url': reverse('page2'), 'next_page_url': reverse('page4')})

def page4(request):
    return render(request, 'page4.html', {'previous_page_url': reverse('page3'), 'next_page_url': reverse('page5')})
def page5(request):
    return render(request, 'page5.html', {'previous_page_url': reverse('page4')})
