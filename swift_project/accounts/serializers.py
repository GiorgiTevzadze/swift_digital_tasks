from django.core.validators import EmailValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import MyAccount as Account


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        write_only_fields = ['password']
        extra_kwargs = {
            'password': {
                'style': {'input_style': 'password'},
                'write_only': True
            },
            'email': {
                'validators': [
                    EmailValidator,
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message='This Email already exist'
                    )
                ]
            }
        }

    def save(self, *args, **kwargs):  # it does not takes any '*args' and '**kwargs'
        account = Account(email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password[0] != password2[0]:
            raise serializers.ValidationError({'password': 'Password does not match'})
        account.set_password(password)
        account.save()
        return account
