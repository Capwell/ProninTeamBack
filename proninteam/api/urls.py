from django.urls import path, include

urlpatterns = [
    path('v1/', include('offers.urls')),
    path('v1/', include('users.urls'))
]

app_name = 'api'
