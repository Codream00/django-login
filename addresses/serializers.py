from rest_framework import serializers
from .models import Addresses


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ["userId", "password", "name", "created"]
