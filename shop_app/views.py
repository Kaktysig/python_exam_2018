from django.http import HttpResponse
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Customer, Goods_Variation, Cart, Order
from .serializers import (
    ProfileSerializer,
    ShopSerializer,
    CartSerializer,
    OrderSerializer,
)


class ProfileView(GenericViewSet,
                  mixins.ListModelMixin,  # TODO: remove after tests are completed
                  mixins.CreateModelMixin):
    serializer_class = ProfileSerializer
    queryset = Customer.objects.all()


class ShopView(GenericViewSet,
               mixins.ListModelMixin):
    serializer_class = ShopSerializer
    queryset = Goods_Variation.objects.all()


class CartView(GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class OrderView(GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()