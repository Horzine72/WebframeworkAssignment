from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact, name='contact'),
    path('tracking/', views.tracking, name='tracking'),
    path('help/', views.help, name='help'),
    path('invoices/', views.view_invoices, name='view_invoices'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('invoices/add/', views.add_invoice, name='add_invoice'),
    path('invoices/manage/', views.manage_invoices, name='manage_invoices'),
]