from django.urls import path, include
from rest_framework import routers

from cases.api.views import CaseViewSet

router = routers.DefaultRouter()
router.register('cases', CaseViewSet, basename='cases')

urlpatterns = [
    path('', include(router.urls))
]

app_name = 'cases'
