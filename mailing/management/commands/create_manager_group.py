from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Create manager group with specific permissions'

    def handle(self, *args, **kwargs):
        # Create the group
        manager_group, created = Group.objects.get_or_create(name='Manager')

        if created:
            self.stdout.write(self.style.SUCCESS('Manager group created'))

        # Define permissions
        permissions = [
            Permission.objects.get(codename='view_mailing'),
            Permission.objects.get(codename='view_user'),
            Permission.objects.get(codename='block_user'),
            Permission.objects.get(codename='deactivate_mailing')
        ]

        # Add permissions to the group
        manager_group.permissions.set(permissions)
        manager_group.save()

        self.stdout.write(self.style.SUCCESS('Permissions assigned to Manager group'))