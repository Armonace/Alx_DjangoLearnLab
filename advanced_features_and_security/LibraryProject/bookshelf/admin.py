from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
from django.contrib import admin
from .models import Book

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to show in list view
    list_display = (
        'username', 'email', 'first_name', 'last_name', 
        'date_of_birth', 'is_staff'
    )

    # Fields to filter by
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # Fieldsets: Group fields in the detail/edit form
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )

    # Fields for the 'Add user' form in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Info'), {
            'classes': ('wide',),
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )


# app_name/admin.py

from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    
