from django.urls import path
from .views import ItemListAPIView

urlpatterns = [
    path('product-list/', ItemListAPIView.as_view(), name='product_list'),
]
