import requests
import json
# from .models import UserTable

serverToken = 'AAAAkQs_DCw:APA91bE4cfIc9yNPQTgrN3dlbNy-ZQnAfhywatLCACIFMcYjkn8oivii3vxuN3QNP7ulNekI8w0xvSJ3zWa-yNhYRAT5C3BnlMlLBKby_J0GnvIFj72TWv3_GUpUq9IkifJEzdip7FbH'

def send_notification_to_user(send_notification_to_user_id, title, body):

    deviceToken = UserTable.objects.get(user_id=send_notification_to_user_id).device_token
    #deviceToken = 'd1t_teA-oTg:APA91bG7mX58W6OgVRytBcu4F8_lbSl4hG2gCU9eRdKzKvNNU4wEWTG8WvbRP_9ThO9aXxDcSiEBXe2mxIor2GBUQoqIwONqVaMrEuLrfScCulpHZGFnNeVHx6-itLBO2iOzBaXy4ecq'

    if deviceToken:
        headers = {
                'Content-Type': 'application/json',
                'Authorization': 'key=' + serverToken,
            }

        body = {'notification': 
                {'title': title, 'body': body},
                'to':deviceToken,
                'priority': 'high',
                #   'data': dataPayLoad,
                }
        response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
        return 1
    return 0