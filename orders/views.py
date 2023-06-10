from rest_framework import generics
from .models import Cart, CartItem
from rest_framework.response import Response
from .serializers import CartSerializer, AddAndRemoveSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class GetCartItemsAPIView(generics.ListAPIView):
    serializer_class = CartSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Cart.objects.filter(client=self.request.user, is_ordered=False)
        return queryset


class AddToCartAPIView(generics.GenericAPIView):
    serializer_class = AddAndRemoveSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        question = self.request.data['question_id']
        my_cart, new_cart = Cart.objects.get_or_create(client=self.request.user, is_ordered=False)
        if my_cart:
            CartItem.objects.create(question_id=question, cart=my_cart)
        if new_cart:
            CartItem.objects.create(question_id=question, cart=new_cart)
        return Response({'message': 'Successfully added'}, status=200)


class RemoveToCartAPIView(generics.GenericAPIView):
    serializer_class = AddAndRemoveSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        question = self.request.data['question_id']
        cart_item = CartItem.objects.filter(question_id=question)
        cart_item.delete()
        return Response({'message': 'Successfully removed'}, status=200)
