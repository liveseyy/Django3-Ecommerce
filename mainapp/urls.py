from django.urls import path

from . import views

urlpatterns = [
    path('', views.test_view, name='base'),
    path('products/<str:ct_model>/<str:slug>/', views.ProductDetailView.as_view(), name='product_detail')
]
