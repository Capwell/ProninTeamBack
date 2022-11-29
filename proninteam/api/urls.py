from django.urls import path, include
from rest_framework import routers

from api.views import RequestViewSet, UsersListViewSet

router = routers.DefaultRouter()
router.register('requests', RequestViewSet, basename='requests')
router.register('users', UsersListViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls))
]

app_name = 'api'
