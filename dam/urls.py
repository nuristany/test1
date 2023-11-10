from. import views
from django.urls import path




urlpatterns = [
    path('', views.home, name='home'),
    path('register_donor/', views.register_donor, name='register_donor'),
    path('thank_you/', views.thank_you, name='thank_you'),
]