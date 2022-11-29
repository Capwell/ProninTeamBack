from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from api.serializers import CreateRequestSerializer, UserListSerializer
from users.models import User


class RequestViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = CreateRequestSerializer


class UsersListViewSet(GenericViewSet, ListModelMixin):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()
