from django.urls import path

from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('products/<str:ct_model>/<str:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
]
