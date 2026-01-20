from django.urls import path,include
from store import views

urlpatterns = [
    path('',views.home),
    path("add-product/",views.add_product),
]