from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Attribute, AttributeName, AttributeValue, Catalog, Image, Product, ProductAttributes, ProductImage, MODELS_DICT
from .serializers import (
    AttributeSerializer, AttributeNameSerializer, AttributeValueSerializer, CatalogSerializer, ImageSerializer,
    ProductAttributesSerializer, ProductImageSerializer, ProductSerializer, SERIALIZERS_DICT
)
from django.db import models

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.core.exceptions import ValidationError
from django.http import Http404

class ImportDataView(APIView):
    parser_classes = [JSONParser]
    def post(self, request, *args, **kwargs):
        #Getting the request data and creating saved_data dict which we`ll return
        data = request.data
        saved_data = {}

        #Iterating through data
        for item in data:   
            
            #Getting all fields and values in model
            for model_name, model_data in item.items():

                try:
                    #Trying to get the model by its name
                    model = MODELS_DICT.get(model_name)
                    if not model:
                        print("Model not found")
                        continue
                    
                    #Trying to get serializer by its name
                    serializer_class = SERIALIZERS_DICT.get(model_name.lower())
                    if not serializer_class:
                        print("serializer not found")
                        continue
                    
                    try:
                        #Trying to update the fields. 
                        instance = model.objects.get(pk=model_data.get("id"))
                        self.update_model_instance(instance, model_data)
                        print("updated instance", model_name,  model_data)
                        continue
                    except Exception as E:
                        pass
                    
                    #Validating the fields so the model we use has all the data
                    if not self.validate_fields(model, model_data):
                        continue
                    
                    #Serializing the data and saving it to db and saved_data
                    serializer = serializer_class(data=model_data)
                    if serializer.is_valid():
                        saved_obj = serializer.save()
                        saved_data.setdefault(model_name, []).append(serializer.data)
                    else:
                        print("serializer is not valid", serializer.errors)
                        continue

                except Exception as E:
                    print("Some exception ", E)
        
        return Response(saved_data, status=status.HTTP_201_CREATED)
    
    def validate_fields(self, model, data):
        try:
            for key in data.keys():
                #Validating fields by getting every field of data and checking if model contains this field
                if not hasattr(model, key):
                    return False
            return True
        except Exception as E:
            print(E)
            return False
        
    def update_model_instance(self, instance, update_dict):
        for field, value in update_dict.items():
            if '__' in field:
                
                field_name, lookup = field.split('__', 1)
                related_model = getattr(instance, field_name)
                self.update_model_instance(related_model, {lookup: value})
            else:
                #Getting the field we`re going to update
                field_object = instance._meta.get_field(field)

                #Updating the field. Checking all cases of field type.
                if isinstance(field_object, models.ForeignKey):
                    related_model = field_object.related_model
                    value = related_model.objects.get(pk=value)
                if isinstance(field_object, models.ManyToManyField):
                    field = getattr(instance, field)
                    field.set(value)
                else:
                    setattr(instance, field, value)

        instance.save()
class DetailModelView(generics.ListAPIView):
    def get_queryset(self):
        #Getting model objects by name of model
        model_name = self.kwargs['model_name']
        model = MODELS_DICT.get(model_name)
        if not model:
            raise Http404("Model not found")
        return model.objects.all()
    
    def get_serializer_class(self):
        #Getting serializer object by its name
        model_name = self.kwargs['model_name']
        serializer_class = SERIALIZERS_DICT.get(model_name.lower())
        if not serializer_class:
            return None
        
        return serializer_class
    
    def get(self, request, *args, **kwargs):
        try:
        #Getting model objects and serializer. Then serialize and return response
            queryset =  self.get_queryset()
            serializer_class = self.get_serializer_class()
            if not serializer_class:
                raise Http404("Serializer not found")
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise Http404("Not found the objects")


class DetailItemView(generics.RetrieveAPIView):
    def get_object(self):
        try:
            #Getting the model by its name
            model_name = self.kwargs['model_name']
            model = MODELS_DICT.get(model_name)
            if not model:
                raise Http404("Model not found")
            
            #Getting the object and returning it
            obj_id = self.kwargs['pk']
            obj = model.objects.get(pk=obj_id)
            
            return obj
        except Exception as E:
            raise Http404("Object not found")
    
    def get_serializer_class(self):
        model_name = self.kwargs['model_name']
        serializer_class = SERIALIZERS_DICT.get(model_name.lower())
        if not serializer_class:
            raise Http404("Serializer not found")
        
        return serializer_class