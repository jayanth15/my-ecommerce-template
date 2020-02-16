from django.urls import path
from .views import items_list, products, checkout
app_name = "cart"

urlpatterns = [
    path("",items_list, name ="items_list"),
    path("products/",products, name="products"),
    path("checkout/",checkout, name="checkout"),
]