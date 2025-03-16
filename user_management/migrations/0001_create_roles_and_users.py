from django.db import migrations
from django.contrib.auth.hashers import make_password
from django.core.management import call_command

def create_roles_and_users(apps, schema_editor):
    print("Creating roles and users...")

    call_command("migrate", "auth") 

    # Get models through apps (to avoid direct model access in migrations)
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    User = apps.get_model("auth", "User")

    # Define roles and permissions
    role_permissions = {
        "Manager": ["add_product", "change_product", "delete_product", "view_product"],  # Full CRUD
        "User": ["add_product", "change_product", "delete_product"],  # CRU
        "Public": ["view_product"],  # Read-only
    }

    # Create roles and assign permissions
    role_groups = {}
    for role_name, perm_codes in role_permissions.items():
        group, created = Group.objects.get_or_create(name=role_name)
        print(f"✅ Group '{role_name}' created: {created}")

        for perm_code in perm_codes:
            permission = Permission.objects.filter(codename=perm_code).first()
            if permission:
                group.permissions.add(permission)
                print(f"✅ Permission '{perm_code}' added to '{role_name}'")
            else:
                print(f"⚠️ Warning: Permission '{perm_code}' not found.")

        role_groups[role_name] = group

    # Create users and assign them to roles
    user_data = [
        {"username": "admin", "email": "admin@example.com", "password": "admin123", "is_superuser": True, "is_staff": True, "group": None},
        {"username": "manager", "email": "manager@example.com", "password": "manager123", "group": "Manager"},
        {"username": "user", "email": "user@example.com", "password": "user123", "group": "User"},
        {"username": "public", "email": "public@example.com", "password": "public123", "group": "Public"},
    ]

    for user_info in user_data:
        user, created = User.objects.get_or_create(username=user_info["username"], defaults={
            "email": user_info["email"],
            "password": make_password(user_info["password"]),
            "is_superuser": user_info.get("is_superuser", False),
            "is_staff": user_info.get("is_staff", False),
        })
        if created and user_info["group"]:
            user.groups.add(role_groups[user_info["group"]])
            print(f"✅ User '{user_info['username']}' assigned to '{user_info['group']}'")

def reverse_migration(apps, schema_editor):
    """Rollback migration by deleting users and groups."""
    Group = apps.get_model("auth", "Group")
    User = apps.get_model("auth", "User")

    Group.objects.filter(name__in=["Manager", "User", "Public"]).delete()
    User.objects.filter(username__in=["admin", "manager", "user", "public"]).delete()

class Migration(migrations.Migration):
    dependencies = [('product_module', '0001_initial')]

    operations = [
        migrations.RunPython(create_roles_and_users, reverse_migration),
    ]
