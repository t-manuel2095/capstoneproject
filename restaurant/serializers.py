from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Menu
        fields = ['id', 'name', 'price', 'menu_item_description']

        def __str__(self):
            return self.name