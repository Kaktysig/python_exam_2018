from django.shortcuts import get_object_or_404
from rest_framework import serializers
import jwt
from rest_framework_jwt.serializers import jwt_payload_handler

from python_exam import settings
from shop_app.models import Customer, Goods_Variation, Cart


class ProfileSerializer(serializers.ModelSerializer):
    cart = serializers.IntegerField(write_only=True, default="")
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = (
            'token',
            'email',
            'username',
            'password',
            'cart',
        )

    def create(self, validated_data):
        user = Customer(
            email=validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        if validated_data['cart'] != "":
            cart = get_object_or_404(Cart, id=validated_data['cart'])
            cart.customer = user
        return user

    def get_token(self, obj):
        payload = jwt_payload_handler(obj)
        token = jwt.encode(payload, settings.SECRET_KEY)
        return token.decode('unicode_escape')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods_Variation
        fields = (
            'id',
            '__str__',
            'description',
            'cost',
        )

class CartSerializer(serializers.ModelSerializer):
    last_cart = serializers.IntegerField(write_only=True, default="")
    customer_email = serializers.EmailField(write_only=True, default="")

    class Meta:
        model = Cart
        fields = (
            'id',
            'last_cart',
            'customer_email',
            'goods',
        )

    def create(self, validated_data):
        if validated_data['last_cart'] != "":
            last_cart = get_object_or_404(Cart, id=validated_data['last_cart'])
            for good in validated_data['goods']:
                last_cart.goods.add(good)
            last_cart.save()
            return last_cart

        if validated_data['customer_email'] != "":
            customer = Customer.objects.filter(email=validated_data['customer_email']).first()
        else:
            customer = Customer()
            customer.save(

            )
        user_cart = Cart(
            customer = customer
        )
        user_cart.save()
        user_cart.goods = validated_data['goods']
        user_cart.save()
        return user_cart


