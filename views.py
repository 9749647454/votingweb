from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contact(request):
     return  HttpResponse("hi welcome to the votingcontact page and the contact details are as follws ")

