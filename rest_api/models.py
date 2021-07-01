import json

from django.db import models 

from django.utils import timezone
from datetime import datetime
from django.core.validators import RegexValidator
from .constants import *

from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from mysite import settings

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

#UTILS [START] 
class GlobalSettingTable(models.Model):
    gs_id = models.AutoField(db_column='gs_id', primary_key=True)
    gs_name = models.CharField(max_length=100, db_column='gs_name')
    gs_value = models.TextField(db_column='gs_value', blank = True) 
    is_active = models.CharField(db_column='is_active',  default='N', max_length=10, choices=((1, "Y"), (2, "N")), help_text="'Y' or 'N'")
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now) 
    status    = models.CharField(max_length=100, db_column='status')

    def __str__(self):
        role_data = {}
        role_data['gs_id'] = self.gs_id
        role_data['gs_name'] = self.gs_name
        role_data['gs_value'] = self.gs_value
        role_data['is_active'] = self.is_active
        role_data['create_at'] = str(self.create_at)
        role_data['status'] = self.status

        return json.dumps(role_data)
 
    
    class Meta:
        db_table = "GLOBAL_SETTING"



class UserLoginTable(models.Model):
    user_id = models.AutoField(db_column='user_id', primary_key=True) 
    user_name = models.CharField(max_length=500, db_column='user_name')
    last_name = models.CharField(max_length=500, db_column='last_name')
    email = models.EmailField(db_column='email', unique=True)
    phone = models.CharField(max_length=100, db_column='phone', unique=True)
    gender = models.CharField(max_length=500, db_column='gender')
    password = models.CharField(max_length=500, db_column='password') 
    profile_img = models.CharField(max_length=500, db_column='profile_img', null=True, blank=True)
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    comment   = models.CharField(max_length=500, db_column='comment')
    status    = models.CharField(max_length=100, db_column='status')
    address = models.CharField(max_length=500,null=True, db_column='address')
    state = models.CharField(max_length=500,null=True, db_column='state')
    city = models.CharField(max_length=500,null=True, db_column='city')
    token = models.CharField(max_length=800,null=True, db_column='token')

    

    def __str__(self):
        table_data = {}
        table_data['user_id'] = self.user_id    
        table_data['user_name'] = self.user_name  
        table_data['last_name'] = self.last_name
        table_data['email'] = self.email
        table_data['phone'] = self.phone
        table_data['gender'] = self.gender
        table_data['password'] = self.password 
        table_data['profile_img'] = self.profile_img 
        table_data['create_at'] = str(self.create_at)
        table_data['comment'] = self.comment
        table_data['status'] = self.status 
        table_data['address'] = self.address 
        table_data['state'] = self.state 
        table_data['city'] = self.city 
        table_data['token'] = self.token 

        return json.dumps(table_data)
 
    class Meta:
        db_table = "USER_LOGIN"  


class CreateHouseTable(models.Model):
    house_id = models.AutoField(db_column='house_id', primary_key=True) 
    house_name = models.CharField(max_length=500, db_column='house_name')
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    comment   = models.CharField(max_length=500, db_column='comment')
    status    = models.CharField(max_length=100, db_column='status')
    user_details = models.ForeignKey(UserLoginTable, related_name='user_details', on_delete=models.CASCADE, help_text="FK on UserLoginTable")
    
    def __str__(self):
        table_data = {}
        table_data['house_id'] = self.house_id    
        table_data['house_name'] = self.house_name    
        table_data['user_details'] = str(self.user_details) 
        table_data['create_at'] = str(self.create_at)
        table_data['comment'] = self.comment
        table_data['status'] = self.status 
         

        return json.dumps(table_data)
 
    class Meta:
        db_table = "CREATE_ HOUSE"


class CreateRoomTable(models.Model):
    room_id = models.AutoField(db_column='room_id', primary_key=True) 
    room_name = models.CharField(max_length=500, db_column='room_name')
    room_img = models.CharField(max_length=500, db_column='room_img', null=True, blank=True)
    room_power_usage    = models.FloatField(max_length=100, db_column='room_power_usage')
    room_saving    = models.FloatField(max_length=100, db_column='room_saving')
    is_motion_on = models.BooleanField(default=False)
    temperature    = models.FloatField(max_length=100, db_column='temperature')
    house = models.ForeignKey(CreateHouseTable, related_name='house', on_delete=models.CASCADE, help_text="FK on CreateHouseTable")
    user_data = models.ForeignKey(UserLoginTable, related_name='user_data', on_delete=models.CASCADE, help_text="FK on UserLoginTable")
    
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    comment   = models.CharField(max_length=500, db_column='comment')
    status    = models.CharField(max_length=100, db_column='status')
    

    def __str__(self):
        table_data = {}
        table_data['room_id'] = self.room_id    
        table_data['room_name'] = self.room_name   
        table_data['room_img'] = self.room_img 
        table_data['house'] = str(self.house) 
        table_data['house_id'] = str(self.house) 
        table_data['user_data'] = str(self.user_data) 
        table_data['room_power_usage'] = str(self.room_power_usage) 
        table_data['room_saving'] = str(self.room_saving) 
        table_data['is_motion_on'] = str(self.is_motion_on) 
        table_data['temperature'] = str(self.temperature) 

        table_data['create_at'] = str(self.create_at)
        table_data['comment'] = self.comment
        table_data['status'] = self.status 
         

        return json.dumps(table_data)
 
    class Meta:
        db_table = "CREATE_ROOM"  


class CreateDeviceTable(models.Model):
    device_id = models.AutoField(db_column='device_id', primary_key=True) 
    hardware_id = models.CharField(max_length=500, db_column='hardware_id', null=False, blank = False, unique=True)

    device_name = models.CharField(max_length=500, db_column='device_name')
    schedule_time_start_epoch = models.CharField(max_length=500, db_column='schedule_time_start_epoch', null=True, blank=True)
    schedule_time_end_epoch = models.CharField(max_length=500, db_column='schedule_time_end_epoch', null=True, blank=True)
    on_from = models.CharField(max_length=500, db_column='on_from', null=True, blank=True)
    schedule_time_start = models.CharField(max_length=500, db_column='schedule_time_start', null=True, blank=True)
    schedule_time_stop = models.CharField(max_length=500, db_column='schedule_time_stop')
    reading = models.CharField(max_length=500, db_column='reading')
    power_usage    = models.FloatField(max_length=100, db_column='power_usage')
    saving    = models.FloatField(max_length=100, db_column='saving')
    is_motion_on = models.BooleanField(default=False)
    device_on = models.BooleanField(default=False)
    schedule_on = models.BooleanField(default=False)
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    comment   = models.CharField(max_length=500, db_column='comment')
    status    = models.CharField(max_length=100, db_column='status')
    
    user_login_id = models.ForeignKey(UserLoginTable, related_name='user_login_id', on_delete=models.CASCADE, help_text="FK on UserLoginTable")
    get_room_id = models.ForeignKey(CreateRoomTable,  related_name='get_room_id', on_delete=models.CASCADE, help_text="FK on CreateRoomTable")



    def __str__(self):
        table_data = {}
        table_data['device_id'] = self.device_id    
        table_data['hardware_id'] = self.hardware_id    
        table_data['device_name'] = self.device_name   
        table_data['schedule_time_start_epoch'] = self.schedule_time_start_epoch   
        table_data['schedule_time_end_epoch'] = self.schedule_time_end_epoch   
        table_data['on_from'] = self.on_from 
        table_data['schedule_time_start'] = str(self.schedule_time_start) 
        table_data['schedule_time_stop'] = str(self.schedule_time_stop) 
        table_data['reading'] = str(self.reading) 
        table_data['power_usage'] = str(self.power_usage) 
        table_data['saving'] = str(self.saving) 
        table_data['is_motion_on'] = str(self.is_motion_on) 
        table_data['device_on'] = str(self.device_on) 
        table_data['schedule_on'] = str(self.schedule_on) 
        table_data['user_login_id_id'] = str(self.user_login_id) 
        table_data['user_login_id'] = str(self.user_login_id) 
        table_data['get_room_id'] = str(self.get_room_id) 
        table_data['get_room_id_id'] = str(self.get_room_id) 

        table_data['create_at'] = str(self.create_at)
        table_data['comment'] = self.comment
        table_data['status'] = self.status 
         

        return json.dumps(table_data)
 
    class Meta:
        db_table = "CREATE_DEVICE"  



class MotionDetectionTable(models.Model):
    motion_device_id = models.AutoField(db_column='motion_device_id', primary_key=True) 
    hardware_id = models.CharField(max_length=500, db_column='hardware_id')
    
    voltage = models.CharField(max_length=500, db_column='voltage')
    current = models.CharField(max_length=500, db_column='current')
    power = models.CharField(max_length=500, db_column='power')
    power_factor = models.CharField(max_length=500, db_column='power_factor')
    frequency = models.FloatField(max_length=500, db_column='frequency')
    motion_detected_time = models.DateTimeField(max_length=100, null=True, db_column='motion_detected_time')
    device_on = models.DateTimeField(db_column='device_on', default=timezone.now)
    device_on = models.DateTimeField(db_column='device_on', default=timezone.now)
    device_off = models.DateTimeField(db_column='device_off', default=timezone.now)
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    comment   = models.CharField(max_length=500, db_column='comment')
    status    = models.CharField(max_length=100, db_column='status')
    
     

    def __str__(self):
        table_data = {}
        table_data['motion_device_id'] = self.motion_device_id    
        table_data['hardware_id'] = self.hardware_id    
        table_data['voltage'] = self.voltage   
        table_data['current'] = self.current 
        table_data['power'] = str(self.power) 
        table_data['power_factor'] = str(self.power_factor) 
        table_data['frequency'] = str(self.frequency) 
        table_data['motion_detected_time'] = str(self.motion_detected_time) 
        table_data['device_on'] = str(self.device_on) 
        table_data['device_off'] = str(self.device_off)  
        table_data['create_at'] = str(self.create_at) 
        table_data['status'] = str(self.status)   
        table_data['comment'] = self.comment 

        return json.dumps(table_data)
 
    class Meta:
        db_table = "MOTION_DETECTION" 


class HistoryTable(models.Model):
    history_id = models.AutoField(db_column='history_id', primary_key=True) 
    event_name = models.CharField(max_length=500, db_column='event_name', null=False, blank = False,)
    device_name = models.CharField(max_length=500, db_column='device_name', null=True)
    action = models.CharField(max_length=500, db_column='action', null=True)
    message = models.CharField(max_length=500, db_column='message', null=False)
    hardware = models.CharField(max_length=500, db_column='hardware', null=True)
    
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    comment   = models.CharField(max_length=500, db_column='comment', null=True)
    status    = models.CharField(max_length=100, db_column='status', null=True)
    user_info = models.ForeignKey(UserLoginTable, related_name='user_info', on_delete=models.CASCADE, help_text="FK on UserLoginTable")
    house_info = models.ForeignKey(CreateHouseTable, related_name='house_info', on_delete=models.CASCADE, help_text="FK on CreateHouseTable")
    
     

    def __str__(self):
        table_data = {}
        table_data['history_id'] = self.history_id    
        table_data['event_name'] = self.event_name    
        table_data['device_name'] = self.device_name   
        table_data['action'] = self.action 
        table_data['message'] = self.message 
        table_data['hardware'] = str(self.hardware) 
        table_data['user_info'] = str(self.user_info) 
        table_data['house_info'] = str(self.house_info) 

          
        table_data['create_at'] = str(self.create_at) 
        table_data['status'] = str(self.status)   
        table_data['comment'] = self.comment 

        return json.dumps(table_data)
 
    class Meta:
        db_table = "HISTORY" 
	

  
