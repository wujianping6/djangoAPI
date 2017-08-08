from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as  _
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    confirm_password =serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields=("id", "username", "email", "password", "confirm_password", "date_joined")

    def create(self, validated_data):
        # 删除重复密码
        del  validated_data['confirm_password']
        validated_data['password']=make_password(validated_data['password'])

        return super(UserRegistrationSerializer,self).create(validated_data)

    def validate(self, attrs):

        if attrs.get('password')!=attrs.get('confirm_password'):
            raise serializers.ValidationError('密码不一致')

        return attrs


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('Unable to login with provided credentials.')
    }

    def __init__(self,*args,**kwargs):
        super(UserLoginSerializer,self).__init__(*args, **kwargs)
        self.user =None
    def validate(self, attrs):
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])

class TockenSerializer(serializers.ModelSerializer):
    acth_tocken = serializers.CharField(source='key')

    class Meta:
        model =Token
        fields=('auth_token',)