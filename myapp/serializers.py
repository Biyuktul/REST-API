from rest_framework import serializers
from .models import Item
class ItemSerialier(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
