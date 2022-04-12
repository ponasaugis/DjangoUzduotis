from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/<int:customer_id>', views.customer, name='customer'),
    path('add_product', views.add_product, name='add_product'),
    path('products', views.products, name='products'),
    path('test', views.test, name='test'),
]