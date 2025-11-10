from django.urls import path
from . import views

urlpatterns = [
    path('test-sync/', views.test_sync_view, name='test_sync'),
    path('test-thread/', views.test_thread_view, name='test_thread'),
    path('test-transaction/', views.test_transaction_view, name='test_transaction'),
]