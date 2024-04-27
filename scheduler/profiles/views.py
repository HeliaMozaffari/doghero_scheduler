from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return render(request, 'registration.html') 

def booking(request):
    return render(request, 'booking.html') 

def schedule(request):
    return render(request, 'schedule.html') 