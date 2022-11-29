from django.urls import path, include
from rest_framework import routers

from users.api.views import UsersListViewSet

router = routers.DefaultRouter()
router.register('users', UsersListViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]

app_name = 'users'
