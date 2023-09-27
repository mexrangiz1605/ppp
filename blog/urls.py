from django.urls import path
from .views import *    

urlpatterns = [
    path('',index,name='index'),
    path('firstfood/', firstfood, name='firstfood'),
    path('secondfood/', secondfood, name='secondfood'),
    path('fastfood/', fastfood, name='fastfood'),
    path('desert/', desert, name='desert'),
    path('contact/', contact, name='contact'),
]