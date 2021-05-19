from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='store'),
    path('product/<str:pid>', product_view, name='store-product-detail'),
    path('cart/', cart_view, name='store-cart'),
    path('checkout/', checkout_view, name='store-checkout'),
    path('update_item/', update_item, name='store-update_item'),
    path('save_checkout/', save_checkout, name='store-save_checkout'),
    path('make_payment/', make_payment, name='store-make_payment'),
    path('invoice/<str:order_id>', get_invoice, name='store-invoice'),
]
