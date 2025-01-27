from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('success/', views.payment_success, name='payment_success'),
]


