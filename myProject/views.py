#from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, 'home.html')
   # return HttpResponse('Home page')

def about(request):
   # return HttpResponse('About page')
    return render(request, 'about.html')
