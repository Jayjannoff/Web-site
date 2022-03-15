from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',)

def hodim(request):
    return render(request,'hodim.html')

def natijalar(request):
    return render(request,'natijalar.html')


def open(request):
    return render(request,'open.html')




def handler404(request,exception= None):
    return render(request,'404.html')


def about(request):
    return render(request,'about.html')
