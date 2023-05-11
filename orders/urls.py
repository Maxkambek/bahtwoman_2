from django.urls import path
from . import views

urlpatterns = [
    path('get-cart/', views.GetCartItemsAPIView.as_view()),
    path('addto-cart/', views.AddToCartAPIView.as_view()),
    path('remove-fromcart/', views.RemoveToCartAPIView.as_view())
]
