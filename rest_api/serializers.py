import datetime

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *

class GlobalSettingTableSerializer(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = GlobalSettingTable
        fields = ('gs_id', 'gs_name', 'gs_value', 'is_active', 'create_at', 'status')
 
class UserLoginTableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserLoginTable
        fields = ('user_id', 'user_name', 'last_name', 'email', 'phone','gender','password', 'profile_img', 'create_at', 'comment', 'status','address','state','city','token')
       

class CreateRoomTableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CreateRoomTable
        fields = ('room_id', 'room_name', 'user_data', 'house', 'house_id', 'room_img', 'room_power_usage', 'room_saving', 'is_motion_on', 'temperature', 'create_at', 'comment', 'status')
       

class GetDeviceTableSerializer(serializers.ModelSerializer):
    get_room_id = CreateRoomTableSerializer(read_only=True, many=False)
    
    class Meta:
        model = CreateDeviceTable
        fields = ('device_id','hardware_id', 'device_name', 'on_from', 'schedule_time_start', 'schedule_time_stop', 'reading', 'power_usage', 'saving', 'is_motion_on', 'device_on', 'schedule_on', 'user_login_id', 'get_room_id', 'get_room_id_id', 'create_at', 'comment', 'status')
       

class CreateDeviceTableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CreateDeviceTable
        fields = ('device_id','hardware_id', 'device_name','schedule_time_start_epoch', 'schedule_time_end_epoch', 'on_from', 'schedule_time_start', 'schedule_time_stop', 'reading', 'power_usage', 'saving', 'is_motion_on', 'device_on', 'schedule_on', 'user_login_id', 'get_room_id', 'get_room_id_id', 'create_at', 'comment', 'status')

   

class MotionDetectionTableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MotionDetectionTable
        fields = ('motion_device_id','hardware_id', 'voltage', 'current', 'power', 'power_factor', 'frequency', 'motion_detected_time', 'device_on', 'device_off', 'create_at', 'status', 'comment')
       
class CreateHouseTableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CreateHouseTable
        fields = ('house_id', 'house_name', 'user_details', 'create_at', 'status', 'comment')
       


class HistoryTableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HistoryTable
        fields = ('history_id', 'user_info','house_info', 'event_name', 'device_name', 'action', 'message', 'hardware',  'create_at', 'status', 'comment')

