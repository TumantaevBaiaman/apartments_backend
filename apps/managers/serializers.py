from rest_framework import serializers
from apps.managers.models import Manager
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email",)


class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Manager
        fields = "__all__"


class ManagerCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Manager
        exclude = ['user']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Пользователь с таким именем уже существует.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.is_active = True
        user.is_manager = True
        user.set_password(password)
        user.save()

        manager = Manager.objects.create(
            user=user,
            number=validated_data['number']
        )

        return manager


class ManagerUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Manager
        fields = "__all__"

    def update(self, instance, validated_data):
        user = User.objects.get(id=instance.user.id)
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.save()

        return super().update(instance, validated_data)