from offers.api.serializers import CreateRequestSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet


class RequestViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = CreateRequestSerializer
