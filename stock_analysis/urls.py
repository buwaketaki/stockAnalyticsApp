
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token  
urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include('basics.urls')),
    path('admin/', admin.site.urls),
    # url('api/', include('basics.urls'))
]
