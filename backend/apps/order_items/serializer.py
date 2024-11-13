from rest_framework import serializers
from .models import Order_items

class Order_itemsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Order_items
    fields = '__all__'