from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'phone_number', 'address')

    def validate(self, data):
        if data.get('email') and data.get('password'):
            user = authenticate(email=data.get('email'), password=data.get('password'))
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
