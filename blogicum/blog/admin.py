from django.contrib import admin

from blog.models import Category
from blog.models import Location
from blog.models import Post

admin.site.empty_value_display = 'Не задано'
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post)
