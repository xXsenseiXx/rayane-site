from django.contrib import admin

# Register your models here.
from .models import user, product, watchlist

admin.site.register(user)
admin.site.register(product)
admin.site.register(watchlist)