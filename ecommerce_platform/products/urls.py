from django.urls import path, include
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]

from rest_framework.routers import DefaultRouter
from .views import ScheduledTaskViewSet

router = DefaultRouter()
router.register(r'scheduled-tasks', ScheduledTaskViewSet, basename='scheduled-task')

urlpatterns = [
    path('', include(router.urls)),
]