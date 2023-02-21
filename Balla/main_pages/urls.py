from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [



    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)