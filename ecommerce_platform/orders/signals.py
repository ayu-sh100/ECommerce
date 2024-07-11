from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order

@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Order Confirmation',
            f'Your order {instance.id} has been placed successfully.',
            'noreply@abc.com',
            [instance.user.email],
            fail_silently=False,
        )
