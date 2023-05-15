from rest_framework import serializers

from .models import NewUser


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'address']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        user = NewUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone_number=validated_data.get('phone_number', ''),
            address=validated_data.get('address', ''),
        )
        return user


class NewSuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'address']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        user = NewUser.objects.create_superuser(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone_number=validated_data.get('phone_number', ''),
            address=validated_data.get('address', ''),
        )
        return user
