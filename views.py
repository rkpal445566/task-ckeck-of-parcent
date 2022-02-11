

from django.shortcuts import render
#from app_1.forms import Student
from django.http import HttpResponse
# Create your views here.
def fun(request):
  
 return render(request,'app_1/home.html')

def fun1(request):
  n1=int(request.GET["num1"])
  n2=int(request.GET["num2"])
  n3=int(request.GET["num3"])

  add1=(n1*n2*n3)/100
  total_rs=n1+add1
  
    
  return render(request,'app_1/pracet.html',{'total':add1,'tlm':total_rs,'amount':n1})