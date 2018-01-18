from django.http import HttpResponse
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Customer, Goods_Variation, Cart
from .serializers import (
    ProfileSerializer,
    ShopSerializer,
    CartSerializer,
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


def base_view(request):
    return HttpResponse("Test travis!")
