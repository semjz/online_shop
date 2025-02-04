from rest_framework import serializers
from .models import Customer, Order, Product


class CustomerSerializer(serializers.ModelSerializer):
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
    products = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field="id", many=True
                                            , required=True)
    total_price = serializers.SerializerMethodField(read_only=True)


    def get_total_price(self, obj):
        return sum(product.price for product in obj.products.all())

    class Meta:
        model = Order
        fields = ["id", "products", "total_price"]


