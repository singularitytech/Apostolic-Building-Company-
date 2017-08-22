from django.conf.urls import include, url
from django.contrib import admin
import blog.urls
from django.conf.urls.static import static
from django.conf import settings
from blog import views

admin.autodiscover()

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)