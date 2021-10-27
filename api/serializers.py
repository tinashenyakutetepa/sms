from rest_framework import serializers
from stock.models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock        
        exclude = ('expiry_date',)