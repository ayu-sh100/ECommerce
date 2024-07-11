from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from rest_framework import viewsets
from django_celery_beat.models import PeriodicTask
from rest_framework.response import Response
from rest_framework.decorators import action

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ScheduledTaskViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'])
    def list_scheduled_tasks(self, request):
        tasks = PeriodicTask.objects.all()
        return Response({'tasks': tasks.values()})