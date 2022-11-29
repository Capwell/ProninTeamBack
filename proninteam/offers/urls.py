from django.urls import path, include
from rest_framework import routers

from offers.api.views import RequestViewSet

router = routers.DefaultRouter()
router.register('requests', RequestViewSet, basename='requests')

urlpatterns = [
    path('', include(router.urls))
]

app_name = 'offers'
