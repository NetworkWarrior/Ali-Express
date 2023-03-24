from django.urls import path
from .views import ProductListView, ProductDetailView, ProductPaymentView, SellProductListView, SellProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('payment/', ProductPaymentView.as_view(), name='product_payment'),
    path('sell/', SellProductListView.as_view(), name='product_sell'),
    path('sell/<int:id>/', SellProductDetailView.as_view(), name='product_sell_detail'),
]

