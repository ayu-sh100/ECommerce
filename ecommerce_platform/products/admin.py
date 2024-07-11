from django.contrib import admin
from .models import Product
from .tasks import bulk_product_upload
from django_celery_beat.models import PeriodicTask

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['bulk_upload_action']

    def bulk_upload_action(self, request, queryset):
        products_data = list(queryset.values())
        bulk_product_upload.delay(products_data)
        self.message_user(request, "Bulk upload task started successfully.")
    bulk_upload_action.short_description = "Bulk upload selected products"

class ScheduledTaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'task', 'enabled', 'last_run_at']
    list_filter = ['enabled', 'task']