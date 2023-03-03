from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.core.management.sql import emit_post_migrate_signal


def add_group_permissions(apps, schema_editor):
    group_permissions = {
        'users-pets-api-read-all': [
            'view_owner',
            'view_person',
            'view_pet'
        ],
        'users-pets-api-create-all': [
            'add_owner',
            'add_person',
            'add_pet'
        ],
        'users-pets-api-update-all': [
            'change_owner',
            'change_person',
            'change_pet'
        ],
        'users-pets-api-delete-all': [
            'delete_owner',
            'delete_person',
            'delete_pet'
        ],
        'users-pets-api-read-not-sensitive': [
            'view_pet'
        ],
        'users-pets-api-create-not-sensitive': [
            'add_pet'
        ],
        'users-pets-api-update-not-sensitive': [
            'change_pet'
        ],
        'users-pets-api-delete-not-sensitive': [
            'delete_pet'
        ]
    }

    db_alias = schema_editor.connection.alias
    emit_post_migrate_signal(2, False, db_alias)

    for group_name in group_permissions:

        group, created = Group.objects.get_or_create(name=group_name)

        for permission_name in group_permissions[group_name]:

            permission, created = Permission.objects.get_or_create(codename=permission_name)
            group.permissions.add(permission)

        group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '__latest__'),
        ('auth', '__latest__'),
        ('users_pets_api', '0004_alter_owner_managers_alter_pet_managers'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions)
    ]
