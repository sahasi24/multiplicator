from django.urls import path 
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("mul",views.mul,name="mul"),
    
]
