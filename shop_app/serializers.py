from rest_framework import serializers
import jwt
from rest_framework_jwt.serializers import jwt_payload_handler

from python_exam import settings
from shop_app.models import Customer, Goods_Variation, Cart


class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = (
            'token',
            'email',
            'username',
            'password',
        )

    def create(self, validated_data):

        user = Customer(
            email=validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def get_token(self, obj):
        payload = jwt_payload_handler(obj)
        token = jwt.encode(payload, settings.SECRET_KEY)
        return token.decode('unicode_escape')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods_Variation
        fields = (
            '__str__',
            'description',
            'cost',
        )

class CartSerializer(serializers.ModelSerializer):


    class Meta:
        model = Cart
        # exclude = ()
        fields = (
            'goods',
        )