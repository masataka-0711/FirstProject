from django.contrib import admin
from .models import(
    ProductTypes, Traders, Products,
    ProductPictures
)
# Register your models here.
admin.site.register(
    [ProductTypes, Traders, Products,ProductPictures]
)