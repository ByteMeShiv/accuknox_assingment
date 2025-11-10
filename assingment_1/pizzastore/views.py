import time
import threading
from django.db import transaction
from django.http import HttpResponse
from .models import PizzaStore, Customer, Order

def test_sync_view(request):
    print("\n SYNC TEST ")
    start = time.time()
    print("Main: Ordering pizza...")
    PizzaStore.objects.create(name="Headquarters", size="Large")
    print("Main: Order received.")
    print(f"Total time: {time.time() - start:.2f}s")
    return HttpResponse("Sync test complete. Check console.")

def test_thread_view(request):
    print("\n THREAD TEST ")
    print(f"  Main running in thread: {threading.get_ident()}")
    Customer.objects.create(name="Shivam Kushwaha")
    return HttpResponse("Thread test complete. Check console.")

def test_transaction_view(request):
    print("\n TRANSACTION TEST ")
    try:
        with transaction.atomic():
            print("  Main: Placing order...")
            Order.objects.create(amount=50)
            print("  Main: Order placed (should not reach here).")
    except Exception as e:
        print(f"  Main: Caught expected error: {e}")
    print(f"  Main: Final orders in DB: {Order.objects.count()}")
    return HttpResponse("Transaction test complete. Check console.")