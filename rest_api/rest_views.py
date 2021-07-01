import calendar
import os
import time
from io import BytesIO
from random import randrange

import requests
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from PIL import Image
from rest_framework import (filters, generics, permissions, renderers,
                            response, schemas, viewsets)
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from werkzeug.utils import secure_filename

from rest_api.permissions import IsOwnerOrReadOnly
from rest_api.serializers import *
from django.db.models import Sum 
from .models import *
from .utils import *
from .api_algorithm import *

from rest_framework.permissions import IsAuthenticated # new import



TOMCAT_PATH = "/opt/apache-tomcat-9.0.27/webapps/"


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Rest API')
    return response.Response(generator.get_schema(request=request))

def index(request):
    return HttpResponse("Rest API")


#[Start] Override one of the pagination classes, and seting the attributes..
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

#[end]

#[START] Rest api for swagger documentation..

class GlobalSettingTableList(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = GlobalSettingTable.objects.all()    
    serializer_class = GlobalSettingTableSerializer

#[END] 

class UserLoginTableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = UserLoginTable.objects.all()
    serializer_class = UserLoginTableSerializer
    permission_classes = (IsAuthenticated,) #permission classes

    # def create(self, request, *args, **kwargs):

    #     print(request.data,'####')


    #Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    
    filterset_fields = ('user_id','email','password')
    #Apply Sorting..
    ordering_fields = ['create_at']
    #Serchalble Fields..
    search_fields = ['status']

class CreateRoomTableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = CreateRoomTable.objects.all()
    serializer_class = CreateRoomTableSerializer
    permission_classes = (IsAuthenticated,) #permission classes


    #Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    
    filterset_fields = ('room_id','user_data', 'house_id','room_name','is_motion_on')
    #Apply Sorting..
    ordering_fields = ['create_at']
    #Serchalble Fields..
    search_fields = ['status']



class GetDeviceTableSerializer(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = CreateDeviceTable.objects.all()
    serializer_class = GetDeviceTableSerializer
    permission_classes = (IsAuthenticated,) #permission classes


    #Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    
    filterset_fields = ('device_id','hardware_id','user_login_id','get_room_id','device_on','device_name')
    #Apply Sorting..
    ordering_fields = ['create_at']
    #Serchalble Fields..
    search_fields = ['status']


class CreateDeviceTableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = CreateDeviceTable.objects.all()
    serializer_class = CreateDeviceTableSerializer
    permission_classes = (IsAuthenticated,) #permission classes


    #Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    
    filterset_fields = ('device_id','hardware_id','user_login_id','get_room_id','device_name')
    #Apply Sorting..
    ordering_fields = ['create_at']
    #Serchalble Fields..
    search_fields = ['status']


class MotionDetectionTableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = MotionDetectionTable.objects.all()
    serializer_class = MotionDetectionTableSerializer
    permission_classes = (IsAuthenticated,) #permission classes


    #Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    
    filterset_fields = ('motion_device_id','hardware_id','device_on','device_off')
    #Apply Sorting..
    ordering_fields = ['create_at']
    #Serchalble Fields..
    search_fields = ['status']


class CreateHouseTableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides details of house.
    """
    queryset = CreateHouseTable.objects.all()
    serializer_class = CreateHouseTableSerializer
    permission_classes = (IsAuthenticated,) #permission classes


    #Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    
    filterset_fields = ('house_name','user_details','house_id')
    #Apply Sorting..
    ordering_fields = ['create_at']
    #Serchalble Fields..
    search_fields = ['status']


class HistoryTableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides details of house.
    """
    queryset = HistoryTable.objects.all()
    serializer_class = HistoryTableSerializer
    permission_classes = (IsAuthenticated,) #permission classes


    #Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    
    filterset_fields = ('hardware', 'house_info', 'user_info', 'device_name', 'event_name')
    #Apply Sorting..
    ordering_fields = ['create_at']
    #Serchalble Fields..
    search_fields = ['status']


@api_view(['GET','POST'])
def git_pull(request):

    PATH_OF_GIT_REPO = '.git'
    COMMIT_MESSAGE = 'refresh'
    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add(update=True)
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.pull()

    
    return HttpResponse("success",status=200)


@api_view(['GET','POST'])
def git_push(request):
  
    PATH_OF_GIT_REPO = '.git'
    COMMIT_MESSAGE = 'refresh'
    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add(update=True)
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()
   
    return HttpResponse("success",status=200)

