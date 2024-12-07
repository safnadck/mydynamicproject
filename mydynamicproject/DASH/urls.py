from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('services/', views.services_view, name='services'),
    path('support/', views.support_view, name='support'),
    path('faq/', views.faq_view, name='faq'),
]
