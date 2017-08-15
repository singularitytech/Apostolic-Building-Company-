from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.http import HttpResponse
from django.contrib.auth.models import User
from tastypie import fields
from .models import *
from django.core.serializers import json  
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from django.conf import settings
from tools import *
import json as bases
import simplejson


from tastypie.serializers import Serializer 
 


class PrettyJSONSerializer(Serializer): 
    json_indent = 4 

    def to_json(self, data, options=None): 
        options = options or {} 
        data = self.to_simple(data, options) 
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent) 


class BlogResource(ModelResource):

	class Meta:
		queryset=Blog.objects.all()
		resource_name= 'practice'
		fields=['author', 'title', 'discription', 'model_pic', 'content', 'created_date', 'published_date']
		serializer = PrettyJSONSerializer()
		allowed_methods=('get')
		limit=100

		#authentication = BasicAuthentication()
		#authorization = DjangoAuthorization()
