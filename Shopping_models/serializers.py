from rest_framework import serializers
from Shopping_models.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        