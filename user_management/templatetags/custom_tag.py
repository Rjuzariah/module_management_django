from django import template

register = template.Library()

@register.filter(name='is_manager_or_admin')
def is_manager_or_admin(user):
    # Check if the user is an admin (is_staff) or belongs to the "manager" group
    return user.is_staff or user.groups.filter(name="manager").exists()
