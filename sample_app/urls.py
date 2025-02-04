from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ProductViewSet, CustomerListView


router = DefaultRouter()

router.register('orders', OrderViewSet, basename="orders")

router.register('products', ProductViewSet, basename="products")

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerListView.as_view(), name='customer-detail'),
]