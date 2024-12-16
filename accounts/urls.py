from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('landing/', views.landing, name='landing'),
    path('logout/', views.user_logout, name='logout'),  # Logout path
]
