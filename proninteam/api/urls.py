from django.urls import path, include

urlpatterns = [
    path('v1/', include('offers.urls')),
    path('v1/', include('users.urls')),
    path('v1/', include('cases.urls'))
]

app_name = 'api'
