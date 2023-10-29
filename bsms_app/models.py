from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self): 
        return self.name

class Book (models.Model) :
    status_book = [
        ("available","available"),
        ("rental","rental"),
        ("sold","sold"),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,null=True,blank=True)
    book_photo = models.ImageField(upload_to="nook_photo",null=True,blank=True)
    author_photo = models.ImageField(upload_to="author_photo",null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    pages = models.IntegerField(null=True,blank=True)
    rental_price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rental_period = models.IntegerField(null=True,blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices=status_book,null=True,blank=True)
    category = models.ForeignKey(Category,related_name="book_category",on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self): 
        return self.title