from django.contrib import admin

# Register your models here.
from .models import user, product

admin.site.register(user)
admin.site.register(product)