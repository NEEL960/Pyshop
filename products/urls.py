from django.urls import path
from . import views
# /products
# /products/new/1

urlpatterns = [
    path('',views.index),
    path('new', views.index)
]

