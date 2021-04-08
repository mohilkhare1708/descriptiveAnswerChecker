from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'layouts/home.html', {'title': 'Home'})

def access_denied(request):
    print("hey")
    return render(request, 'layouts/accessDenied.html', {'title': 'Access Denied'})