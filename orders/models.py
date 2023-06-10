from django.db import models
from accounts.models import User
from main.models import Question


class Cart(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)

    @property
    def get_cart_total(self):
        cart_items = self.cart_items.all()
        total = sum([item.get_total for item in cart_items])
        return total

    def __str__(self):
        return f'order of {self.client} (id: {self.id})'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, related_name='cart_items')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='cart_questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_total(self):
        return self.question.price


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'order of {self.client} (id: {self.id})'
