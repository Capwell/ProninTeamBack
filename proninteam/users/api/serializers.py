from rest_framework import serializers
from users.models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('title',)


class UserListSerializer(serializers.ModelSerializer):
    main_role = RoleSerializer()
    other_roles = RoleSerializer(many=True)

    class Meta:
        model = User
        fields = ('main_role', 'other_roles', 'photo',
                  'first_name', 'last_name')
