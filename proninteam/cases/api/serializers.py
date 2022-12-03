from rest_framework import serializers

from cases.models import Case


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('title', 'hex_color', 'logo', 'is_on_main_page',
                  'is_visible', 'slug', 'text')
