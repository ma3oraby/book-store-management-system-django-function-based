from django.shortcuts import render

# Create your views here.

def index (request) :
    return render (request , 'bsms_app/index.html')

def books (request) :
    return render (request, 'bsms_app/books.html')