from django.contrib import admin

# Register your models here.

from listing.models import Product

admin.site.register(Product)