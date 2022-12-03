from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from offers.models import Offer

# CAPTCHA_SECRET_KEY = os.getenv('CAPTCHA_SECRET_KEY')


class CreateRequestSerializer(serializers.ModelSerializer):
    captcha_token = serializers.CharField(write_only=True)

    class Meta:
        model = Offer
        fields = ('name', 'communicate', 'message', 'file',
                  'is_agreed', 'captcha_token')

    def validate(self, attrs):
        is_agreed = attrs.get('is_agreed')
        file = attrs.get('file')
        message = attrs.get('message')
        if not is_agreed:
            raise ValidationError(
                'Вы должны согласиться на обработку персональных данных!'
            )
        if file is None and message is None:
            raise ValidationError(
                'Вы должны либо прикрепить файл, либо написать сообщение!'
            )
        return attrs

    @atomic
    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        instance.send_offer_email()
        return instance
