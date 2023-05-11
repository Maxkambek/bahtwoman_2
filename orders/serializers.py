from .models import Cart, CartItem, Order
from rest_framework import serializers
from main.serializers import QuestionListSerializer


class CartItemSerializer(serializers.ModelSerializer):
    question = QuestionListSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'question', 'created_at']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['cart_items', 'get_cart_total']


class AddAndRemoveSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ['question_id']
