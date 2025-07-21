from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # <-- LoginView.as_view(template_name=...)
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),  # <-- LogoutView.as_view(template_name=...)
    path('register/', views.register, name='register'),
]
