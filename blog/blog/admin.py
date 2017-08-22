from django.contrib import admin
from .models import *
from ckeditor.fields import RichTextField

class BlogAdmin(admin.ModelAdmin):
    body = RichTextField()
    filter = ( 'title')
    search_fields = ['title']
    list_display = ['title']
    list_filter = ['created_date']
    
    class Meta:
        model = Blog





admin.site.register(Blog, BlogAdmin)
