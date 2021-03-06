from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.vendors, name='vendors'),
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),
    path('<int:pk>/delete', views.delete_vendor, name='delete_vendor'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:pk>', views.edit_product, name='edit_product'),
    path('delete-product/<int:pk>', views.delete_product, name='delete_product'),
    path('delete-order/<int:pk>', views.delete_order, name='delete_order'),
    path('edit-order/<int:pk>', views.edit_order, name='edit_order'),


    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),


]