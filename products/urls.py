from django.urls import path
from .views import ProductListView, ProductDetailView, ProductPaymentView, SellProductListView, CheckoutView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('checkout/<int:id>/', CheckoutView.as_view(), name='checkout_payment'),
    path('payment/', ProductPaymentView.as_view(), name='product_payment'),
    path('sell/', SellProductListView.as_view(), name='product_sell'),
]

