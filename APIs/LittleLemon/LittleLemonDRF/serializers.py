from .models import MenuItem
from rest_framework import serializers

class MenuItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        extra_kwargz = {
            'key': {'inner_key': 'value'},
            'key':{'inner_key':'value'}
        }
