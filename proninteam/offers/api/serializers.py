from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from offers.models import Offer


class CreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('name', 'communicate', 'message', 'file', 'is_agreed')

    def validate(self, data):
        is_agreed = self.initial_data.get('is_agreed')
        file = self.initial_data.get('file')
        message = self.initial_data.get('message')
        if not is_agreed:
            raise ValidationError(
                'Вы должны согласиться на обработку персональных данных!'
            )
        if file is None and message is None:
            raise ValidationError(
                'Вы должны либо прикрепить файл, либо написать сообщение!'
            )
        return data

    @atomic
    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        instance.send_offer_email()
        return instance
