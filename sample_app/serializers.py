from rest_framework import serializers
from .models import Customer, Order, Product

class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=True)
    user_name = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(queryset=Customer.objects.all(), slug_field="id", required=True)
    products = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field="id", many=True
                                            , required=True)

    class Meta:
        model = Order
        fields = '__all__'


