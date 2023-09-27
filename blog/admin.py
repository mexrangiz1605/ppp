from django.contrib import admin
from .models import *
from .forms import *
from .forms import ContactForm


# Register your models here.


admin.site.site_header = " GOID | Good Food | Admin "


@admin.register(Food)   
class FoodAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'image',
        'about',
        'ingredient',
        'price',
    )

    list_display = ('title', 'image', 'about', 'ingredient', 'price')


@admin.register(Secondfood)
class SecondfoodAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'image',
        'about',
        'ingredient',
        'price',
    )

    list_display = ('title', 'image', 'about', 'ingredient', 'price')


@admin.register(Fastfood)
class FastfoodAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'image',
        'about',
        'ingredient',
        'price',
    )

    list_display = ('title', 'image', 'about', 'ingredient', 'price')


@admin.register(Desert)
class DesertAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'image',
        'about',
        'ingredient',
        'price',
    )

    list_display = ('title', 'image', 'about', 'ingredient', 'price')

    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = (
        'fullname',
        'email',
        'phonenumber',
        'message',
    )

    list_display = ('fullname', 'email', 'phonenumber', 'message')


