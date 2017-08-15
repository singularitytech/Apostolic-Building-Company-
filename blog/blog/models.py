from __future__ import absolute_import
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField




class Keywords(models.Model):
    class Meta():
        db_table = 'keywords'
        verbose_name_plural = "keywords"
        verbose_name = "keywords"

    name = models.TextField(max_length=50, unique=True, verbose_name=u'Search')

    def __str__(self):
        return self.name


class Category(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name_plural = "categories"
        verbose_name = "category"
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=150, verbose_name="category")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_py = ['name']

    def __str__(self):
        return self.name


mptt.register(Category, order_insertion_by=['name'])


class Inserts(models.Model):
    class Meta:
        db_table = 'vkladki'

    link = models.TextField('text field')
    nazvanie = models.TextField('name')

    def __str__(self):
        return self.link


class Genre(MPTTModel):
    name = models.TextField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

class Blog(models.Model):
    
    author = models.ForeignKey('auth.User')
    title = models.CharField('header', max_length=200)
    discription = models.TextField()
    model_pic = models.ImageField(upload_to='pic_folder/', default = 'pic_folder/None/no-img.jpg', verbose_name='blogpics')
    content = RichTextUploadingField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = TreeForeignKey(Category, blank=True, null=True, related_name='catt')
    keywords = models.ManyToManyField(Keywords, related_name="keywordss", related_query_name="keywordss",
                                      verbose_name=u'tagss')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "posts/get/%i/" % self.id
