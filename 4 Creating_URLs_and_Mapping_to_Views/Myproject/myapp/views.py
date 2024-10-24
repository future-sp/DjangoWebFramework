from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Home(request):
    return HttpResponse('Welcome to Little Lemon!')
def About(request):
    return HttpResponse('About us')
def Menu(request):
    return HttpResponse('Menu for Little Lemon')
def Booking(request):
    return HttpResponse('Make a booking')
