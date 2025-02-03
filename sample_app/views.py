from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Customer, Order, Product
from .serializers import CustomerSerializer, OrderSerializer, ProductSerializer


class CustomerView(APIView):
    def get(self, request, *args, **kwargs):
        result = Customer.objects.all()
        serializer = CustomerSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CustomerSerializer)
    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    http_method_names = ("get", "post", "delete")
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            products = serializer.validated_data["products"]

            total_price = sum(product.price for product in products)  # Assuming `price` field exists in `Product`

            order = serializer.save()

            return Response(
                {
                    "order": OrderSerializer(order).data,
                    "total_price": total_price
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(ModelViewSet):
    queryset = Order.objects.all()
    http_method_names = ("get", "post", "put")
    serializer_class = ProductSerializer
