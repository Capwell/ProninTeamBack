from cases.api.views import CaseViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cases', CaseViewSet, basename='cases')

urlpatterns = [
    path('', include(router.urls))
]

app_name = 'cases'
