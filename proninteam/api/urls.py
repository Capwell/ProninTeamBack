from api.views import ping
from django.urls import include, path

urlpatterns = [
    path('', include('offers.urls')),
    path('', include('users.urls')),
    path('', include('cases.urls')),
    path('ping', ping)
]

app_name = 'api'
