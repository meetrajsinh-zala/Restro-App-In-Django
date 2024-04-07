from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.registre, name='redister'),
    path('Delete_Cart/', views.Delete_Cart, name='Delete_Cart'),
]