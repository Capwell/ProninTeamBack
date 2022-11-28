from django.forms.fields import FileField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Request
from users.models import User, Role


class CreateRequestSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, min_length=2)
    communicate = serializers.CharField(required=True, min_length=2)
    message = serializers.CharField(required=False, min_length=20)
    file = FileField(allow_empty_file=False)
    is_agreed = serializers.BooleanField(required=True)

    class Meta:
        model = Request
        fields = ('name', 'communicate', 'message', 'file', 'is_agreed')

    def validate(self, data):
        is_agreed = self.initial_data.get('is_agreed')
        file = self.initial_data.get('file')
        message = self.initial_data.get('message')
        if not is_agreed:
            raise ValidationError('Вы должны согласиться на'
                                  ' обработку персональных данных!')
        if file is None and message is None:
            raise ValidationError('Вы должны либо прикрепить файл,'
                                  ' либо написать сообщение!')
        return data

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        file = validated_data.get('file')
        if file:
            file.open('rb')
            instance.send_request_email(file=file)
            file.close()
            return instance
        instance.send_request_email()
        return instance


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('title', )


class UserListSerializer(serializers.ModelSerializer):
    main_role = serializers.SerializerMethodField()
    other_roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('main_role', 'other_roles', 'photo',
                  'first_name', 'last_name', 'middle_name')

    def get_main_role(self, instance):
        return RoleSerializer(
            instance.roles.all().filter(is_main=True).first()
        ).data

    def get_other_roles(self, instance):
        return RoleSerializer(
            instance.roles.all().filter(is_main=False), many=True
        ).data
