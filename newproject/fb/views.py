from django.shortcuts import render

# Create your views here.

def fb(request):
    return render (request,'fb.html')

def domvalidation(request):
    return render (request,'domvalidation.html')

def val(request):
    return render (request,'val.html')

def calculater(request):
    return render (request,'calculater.html')

def array(request):
    return render (request,'domarray.html')

def firstpush(request):
    return render (request,'firstpush.html')



