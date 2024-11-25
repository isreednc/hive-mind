from django.contrib.auth.models import User, Group

def validate_user_group(user, group_id):
    return user.groups.filter(id=group_id).exists()