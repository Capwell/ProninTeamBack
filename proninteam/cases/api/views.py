from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from cases.models import Case
from cases.api.serializers import CaseSerializer


class CaseViewSet(GenericViewSet, ListModelMixin):
    serializer_class = CaseSerializer

    def get_queryset(self):
        return Case.objects.all()
