from django.urls import path, include
from .views import OrderCreateView, OrderListView, OrderDetailView, OrderDeleteView, OrderUpdateView
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
]

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]