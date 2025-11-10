import time
import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):
    name = models.CharField(max_length=50)

class PizzaStore(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=20)

class Order(models.Model):
    amount = models.IntegerField()


@receiver(post_save, sender=PizzaStore)
def bake_pizza_handler(sender, instance, **kwargs):
    print("Signal: Putting pizza in oven (waiting 3s)...")
    time.sleep(3)
    print("Signal: Pizza is ready.")


@receiver(post_save, sender=Order)
def _post_save_receiver(sender, instance, created, **kwargs):
    if created:
        print("  Signal: Payment failed! Rolling back.")
        raise Exception("Payment Error")


@receiver(post_save, sender=Customer)
def payment_handler(sender, instance, **kwargs):
    print(f"  Signal running in thread: {threading.get_ident()}")