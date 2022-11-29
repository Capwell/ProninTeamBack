from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from users.api.serializers import UserListSerializer
from users.models import User


class UsersListViewSet(GenericViewSet, ListModelMixin):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.prefetch_related('roles')
