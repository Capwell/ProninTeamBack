from django.urls import path, include
from rest_framework import routers

from offers.api.views import RequestViewSet

router = routers.DefaultRouter()
router.register('offers', RequestViewSet, basename='offers')

urlpatterns = [
    path('', include(router.urls))
]

app_name = 'offers'
