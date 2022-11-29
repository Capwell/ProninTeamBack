from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from offers.api.serializers import CreateRequestSerializer


class RequestViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = CreateRequestSerializer
