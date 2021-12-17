from rest_framework import serializers
from .models import Shortener


class ShortenerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shortener
        fields = ['original_url', 'short_code', 'timestamp']
        read_only_fields = ['timestamp', 'short_code']


class ShortenerPremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['original_url', 'short_code', 'timestamp']
        read_only_fields = ['timestamp']
