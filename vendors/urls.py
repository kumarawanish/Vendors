
from django.urls import path
from .views import VendorListView, VendorDetailView, PurchaseOrderListView, PurchaseOrderDetailView

urlpatterns = [
    path('vendors/', VendorListView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('purchase-orders/', PurchaseOrderListView.as_view(), name='purchaseorder-list'),
    path('purchase-orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchaseorder-detail'),
]
