from django.shortcuts import render
from .models import Book , Category 

# Create your views here.

def index (request) :
    context = {
        "categories" : Category.objects.all(),
        "books" : Book.objects.all(), 
    }
    return render (request , 'bsms_app/index.html',context)

def books (request) :
    return render (request, 'bsms_app/books.html')