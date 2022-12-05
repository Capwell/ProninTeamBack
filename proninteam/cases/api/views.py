from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response


from cases.models import Case
from cases.api.serializers import CaseSerializer


class CaseViewSet(GenericViewSet, ListModelMixin):
    serializer_class = CaseSerializer

    def get_queryset(self):
        return Case.objects.filter(is_visible=True)

    @action(
        methods=['GET'],
        detail=False
    )
    def main_page(self, request):
        qs = self.get_queryset().filter(
            is_on_main_page=True
        )
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
