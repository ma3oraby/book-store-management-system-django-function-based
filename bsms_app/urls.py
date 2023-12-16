from django.urls import path 
from .views import index , books , update , delete

urlpatterns = [
    path ('',index , name='index'),
    path ('',index , name='index'),
    path ('books',books , name='books'),
    path("update/<int:id>",update,name="update"),
    path("delete/<int:id>", delete , name="delete"),
]
