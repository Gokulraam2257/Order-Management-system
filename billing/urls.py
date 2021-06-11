from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('custom', views.custom, name='custom'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('products', views.products, name='products'),
    path('customers', views.customers, name='customers'),
    path('order', views.order, name='order'),
    path('info', views.info, name='info'),
    path('logout', views.logout, name='logout')


]
