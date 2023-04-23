from django.contrib import admin

# Register your models here.

from listing.models import Product
from listing.models import Type
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date_in') # liste les champs a afficher

admin.site.register(Product,ProductAdmin)
admin.site.register(Type)