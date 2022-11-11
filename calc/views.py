from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html',{'name':'sahasi'})

# def add(request):
    
#     val1 = int(request.GET["num1"])
#     val2 = int(request.GET["num2"])
    
#     sums = val1 + val2
     
       
#     return render(request, "results.html",{'summ':sums})

# def sub(request):
#     val1 = int(request.GET["num1"])
#     val2 = int(request.GET["num2"])
    
#     dif = val1 - val2
    
    
#     return render(request, "results.html",{'diff':dif})
    

def mul(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    
    pro = val1*val2
    
    return render(request, "results.html",{'prod':pro})

# def div(request):
#     val1 = int(request.GET["num1"])
#     val2 = int(request.GET["num2"])
    
#     quo = val1//val2
    
#     return render(request, "results.html",{'quot':quo})