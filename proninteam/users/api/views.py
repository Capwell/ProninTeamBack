from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from users.api.serializers import UserListSerializer
from users.models import User


class UsersListViewSet(GenericViewSet, ListModelMixin):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.filter(
            is_active=True
        ).prefetch_related(
            'other_roles'
        ).select_related(
            'main_role'
        )
