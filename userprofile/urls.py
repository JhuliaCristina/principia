from django.contrib.auth import views as auth_views 
from django.urls import path
from . import views


principia = 'app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('loja/', views.minha_loja, name='loja'),
    path('minhaconta/', views.minha_conta, name='minhaconta'),
    path('vendors/<int:pk>/', views.vendor_details, name='vendor_details'),
]