from rest_framework import serializers

from users.models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('title',)


class UserListSerializer(serializers.ModelSerializer):
    main_role = serializers.SerializerMethodField()
    other_roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('main_role', 'other_roles', 'photo',
                  'first_name', 'last_name', 'middle_name')

    def get_main_role(self, instance):
        return RoleSerializer(
            instance.roles.filter(is_main=True).first()
        ).data

    def get_other_roles(self, instance):
        return RoleSerializer(
            instance.roles.filter(is_main=False), many=True
        ).data
