# bookshelf/management/commands/setup_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Set up default groups and assign permissions'

    def handle(self, *args, **kwargs):
        Post = apps.get_model('bookshelf', 'Article')  # Replace with your actual app + model name

        permissions = {
            'can_view': Permission.objects.get(codename='can_view'),
            'can_create': Permission.objects.get(codename='can_create'),
            'can_edit': Permission.objects.get(codename='can_edit'),
            'can_delete': Permission.objects.get(codename='can_delete'),
        }

        groups_permissions = {
            'Viewers': ['can_view'],
            'Editors': ['can_view', 'can_create', 'can_edit'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.clear()
            for perm in perms:
                group.permissions.add(permissions[perm])
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' updated with permissions: {perms}"))
