from .models import User, Log, Invoice
from rest_framework import serializers
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q


class LogSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Log
        fields = ['url', 'status', 'method', 'created_at']


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Invoice
        fields = ['id', 'url', 'cost', 'date', 'status']
        read_only_fields = ['id', 'url', 'cost', 'date', 'status']

class UserSettingUpdateSerializer(serializers.Serializer):
    credit = serializers.FloatField(required=False)
    has_api_access = serializers.BooleanField(required=False)
    rate_limiting_value = serializers.IntegerField(required=False)
    


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
        help_text='Leave empty if no change needed.',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'stripe_last4', 'card_brand', 'payment_method_id', 'date_joined', 'password']
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
                request = self.context.get('request')
                if request:
                    update_session_auth_hash(request, instance)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance