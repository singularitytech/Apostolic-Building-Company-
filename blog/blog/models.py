from __future__ import absolute_import
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.

from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


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


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "posts/get/%i/" % self.id
