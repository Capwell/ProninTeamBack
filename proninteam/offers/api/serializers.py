from django.db.transaction import atomic
from offers.api.utils import check_recaptcha
from offers.models import Offer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class CreateRequestSerializer(serializers.ModelSerializer):
    token = serializers.CharField(write_only=True)

    class Meta:
        model = Offer
        fields = ('name', 'communicate', 'message',
                  'file', 'is_agreed', 'token')

    def validate(self, attrs):
        token = attrs.pop('token', False)
        if not check_recaptcha(token):
            raise ValidationError(
                'reCAPTCHA не прошла проверку. Попробуйте снова.'
            )
        is_agreed = attrs.get('is_agreed')
        file = attrs.get('file')
        message = attrs.get('message')
        if not is_agreed:
            raise ValidationError(
                'Вы должны согласиться на обработку персональных данных!'
            )
        if file is None:
            if message is None or message == '':
                raise ValidationError(
                    'Вы должны либо прикрепить файл, либо написать сообщение!'
                )
        return attrs

    @atomic
    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        instance.send_offer_email()
        instance.send_offer_telegram()
        return instance
