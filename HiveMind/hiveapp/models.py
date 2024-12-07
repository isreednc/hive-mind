from django.db import models
from django.contrib.auth.models import User, Group

# max character in each string field
string_max = 200

class Timeline_Node(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE,
        null=True
    )
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def mark_completed(self):
        self.is_complete = True
        self.save()

    def __str__(self):
        return self.user.username
