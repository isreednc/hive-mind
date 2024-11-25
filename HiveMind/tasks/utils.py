from django.contrib.auth.models import User, Group

def validate_user_group(user, group_name):
    return user.groups.filter(name=group_name).exists()