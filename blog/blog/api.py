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



class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields =['first_name','last_name','email','username']
        serializer = PrettyJSONSerializer()
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

class PracticesResource(ModelResource):

	class Meta:
		queryset=Practice.objects.all()
		resource_name= 'practice'
		fields=['name','position']
		serializer = PrettyJSONSerializer()
		limit=100

		#authentication = BasicAuthentication()
		#authorization = DjangoAuthorization()

class PointOfInterestResource(ModelResource):

	class Meta:
		queryset = PointOfInterest.objects.all()
		resource_name = 'point'
		fields=['name','position']


class NewbookingsResource(ModelResource):

	class Meta:
		queryset = PointOfInterest.objects.all()
		resource_name = 'newbookings'
		fields=['patients','practitioner','time_created','distance']
		allowed_methods=('get','post','put, delete ','patch')
		limit=12

class PatientsResource(ModelResource):

	class Meta:
		queryset = PointOfInterest.objects.all()
		resource_name = 'newbookings'
		fields=['user','postion','medicalAid_name' ,'medicalAid_no','id_number']
		serializer = PrettyJSONSerializer()
		limit=100

class PractitionerResource(ModelResource):

	class Meta:
		queryset=Practitioner.objects.all()
		resource_name = 'practitioner'
		fields = ['user','higher','place']
		serializer = PrettyJSONSerializer()
		limit = 100
			
		



