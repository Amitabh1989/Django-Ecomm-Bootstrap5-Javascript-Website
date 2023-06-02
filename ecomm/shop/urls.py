from django.urls import path
from .views import ProductView, ProductDetailView, CheckOutView, SuccessPageView


app_name = "shop"

# URL : shop/
urlpatterns = [
    path("", ProductView.as_view(), name="product"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("checkout/", CheckOutView.as_view(), name="checkout"),
    path("success/", SuccessPageView.as_view(), name="success"),
]
