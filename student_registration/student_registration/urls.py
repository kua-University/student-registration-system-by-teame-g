from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', views.home, name='home'),  # Add this line for the root URL
    path('payment/', include('payment.urls')),
]

