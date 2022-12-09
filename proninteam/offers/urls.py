from django.urls import include, path
from offers.api.views import RequestViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('offers', RequestViewSet, basename='offers')

urlpatterns = [
    path('', include(router.urls))
]

app_name = 'offers'
