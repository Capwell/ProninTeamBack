from django.urls import path, include

urlpatterns = [
    path('', include('offers.urls')),
    path('', include('users.urls')),
    path('', include('cases.urls')),
]

app_name = 'api'
