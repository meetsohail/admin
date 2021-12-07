from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_description', 'product_price', 'product_status', 'created_at', 'updated_at', 'product_stripe_id',  'product_stripe_price_id', 'featured', 'max_keywords', 'max_results', 'check_interval', 'realtime_checks']