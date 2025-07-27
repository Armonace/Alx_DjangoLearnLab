from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # <-- LoginView.as_view(template_name=...)
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),  # <-- LogoutView.as_view(template_name=...)
    path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book')
          # ... add other URL patterns
]
