from django.urls import path
from . import views

urlpatterns=[
path('Admin_Login/', views.Admin_Login,name='Admin_Login'),
path('Admin_Dashboard/', views.Admin_Dashboard,name='Admin_Dashboard'),
path('Admin_Menu/', views.Admin_Menu,name='Admin_Menu'),
path('Admin_Order/', views.Admin_Order,name='Admin_Order'),
path('Add_Menu/', views.Add_Menu,name='Add_Menu'),
path('Update_Menu/', views.Update_Menu,name='Update_Menu'),
path('Delete_Menu/', views.Delete_Menu,name='Delete_Menu'),
]