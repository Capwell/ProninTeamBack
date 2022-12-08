from django.urls import path, include

from api.views import ping


urlpatterns = [
    path('', include('offers.urls')),
    path('', include('users.urls')),
    path('', include('cases.urls')),
    path('ping', ping)
]

app_name = 'api'
