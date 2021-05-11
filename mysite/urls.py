from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

 
from rest_api import rest_views, serializers

router = routers.DefaultRouter()
 
router.register(r'user-login', rest_views.UserLoginTableViewSet, 'user-login')
router.register(r'create-room', rest_views.CreateRoomTableViewSet, 'create-room')
router.register(r'create-device', rest_views.CreateDeviceTableViewSet, 'create-device')
router.register(r'get-device', rest_views.GetDeviceTableSerializer, 'get-device')
router.register(r'get-motion-detection', rest_views.MotionDetectionTableViewSet, 'get-motion-detection')


schema_view = get_schema_view(title='Smart Device Rest API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [ 

    #Rest Api..
    path('', schema_view, name= 'v3.doc'),
    path('api-', include(router.urls)),
    path('docs/', include_docs_urls(title='Smart Device Api')), #-------> documentation of API
    path('api/token', obtain_auth_token, name="auth_token"), #-------> token generation of API
    path('api-auth/', include('rest_framework.urls'))


    # path('git_push/', rest_views.git_push, name='git_push'),
    # path('git_pull/', rest_views.git_pull, name='git_pull'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
