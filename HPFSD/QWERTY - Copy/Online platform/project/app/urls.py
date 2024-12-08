from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='Base'),
    path('Brands/', views.base, name='brands'),

    path('buy_now/', views.base, name='buy_now'),
    path('register/', views.Register, name='Register'),
    path('cart/', views.cart, name='cart'),  # Cart page
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    path('smart_equipments/', views.smart_equipments, name='smart_equipments'),
    path('products/', views.products, name='products'),

    path('seeds/', views.seeds, name='seeds'),

    path('login_first/', views.login_first, name='login_first'),
    path('products/', views.products, name='products'),

    path ('about/',views.about, name='about'),

    path ('equipments/',views.equipments, name='equipments'),



]
