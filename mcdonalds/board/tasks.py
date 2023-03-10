from celery import shared_task
from .models import Order
import time
from datetime import timedelta, datetime



@shared_task
def complete_order(oid):
    order = Order.objects.get(pk=oid)
    order.complete = True
    order.save()


@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i + 1)


@shared_task
def clear_old():
    old_orders = Order.objects.all().exclude(time_in__gt=datetime.utcnow() - timedelta(minutes=5))
    old_orders.delete()
