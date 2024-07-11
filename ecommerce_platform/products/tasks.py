from celery import shared_task
from .models import Product

@shared_task
def bulk_product_upload(products_data):
    for product_data in products_data:
        Product.objects.create(**product_data)
