from mptt.admin import MPTTModelAdmin
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



class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']
    list_display = ['name', 'parent']


class KeywordsAdmin(admin.ModelAdmin):
    fields = ['name']



class InsertsAdmin(admin.ModelAdmin):
    field = ['nazvanie']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Keywords, KeywordsAdmin)
admin.site.register(Inserts, InsertsAdmin)

