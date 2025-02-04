from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from authentication.permissions import IsUser
from .models import Customer, Order, Product
from .serializers import OrderSerializer, ProductSerializer, CustomerSerializer


class CustomerListView(mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    API view that allows:
    - Users (staff or admin) to list and retrieve all customers.
    - Customers to retrieve only their own details.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    # Handles GET /customers/ (list all customers)
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:  # If ID is provided, retrieve specific customer
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        # Allow only staff or superusers to list all customers
        if self.request.user.role == "customer":
            return Customer.objects.filter(user=self.request.user)
        # Customers can retrieve only their own detail
        return Customer.objects.all()


class OrderViewSet(ModelViewSet):
    http_method_names = ("get", "post", "delete")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user.role)
        # Filter orders for the authenticated customer only
        if self.request.user.role == "customer":  # Ensure only customers see their own orders
            return Order.objects.filter(customer__user=self.request.user)
        return Order.objects.all()  # Return no orders for non-customers

    def perform_create(self, serializer):
        # Automatically set the customer to the authenticated user
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(customer=customer)

class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsUser]
    queryset = Product.objects.all()
    http_method_names = ("get", "post", "put")
    serializer_class = ProductSerializer
