from django.urls import path
from .views import ProductView, ProductDetailView


app_name = "shop"

# URL : shop/
urlpatterns = [
    path("", ProductView.as_view(), name="product"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
]
