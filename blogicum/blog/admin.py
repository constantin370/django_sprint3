# ice_cream/admin.py
from django.contrib import admin
from .models import Location, Category, Post

admin.site.empty_value_display = 'Не задано'
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post)
