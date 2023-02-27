from django.urls import path
from webapp.views.products_views import products_views, product_add, product_update, product_view, product_delete, out_of_stock

urlpatterns = [
    path('', products_views, name='home'),
    path('products/add', product_add, name='product_add'),
    path('products/update/<int:pk>', product_update, name='product_update'),
    path('products/view/<int:pk>', product_view, name='product_view'),
    path('products/delete/<int:pk>', product_delete, name='product_delete'),
    path('products/out_of_stock', out_of_stock, name='out_of_stock')
]
