from django.urls import path
from .views import CartView, CartItemAddView, CartItemUpdateView, CartItemRemoveView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', CartItemAddView.as_view(), name='cart-item-add'),
    path('cart/update/<int:pk>/', CartItemUpdateView.as_view(), name='cart-item-update'),
    path('cart/remove/<int:pk>/', CartItemRemoveView.as_view(), name='cart-item-remove'),
]
