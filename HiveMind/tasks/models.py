from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE,
        null=True
    )
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    color = models.TextField(max_length=9, default="#ffdcbd")
    pos_top = models.TextField(max_length=7, default="20px")
    pos_left = models.TextField(max_length=7, default="20px")

    def mark_completed(self):
        self.is_complete = True
        self.save()

    def __str__(self):
        return self.user.username

class Reply(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content= models.TextField()

class Timeline_Node(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
         return f"Note: {self.note.content[:30]} by {self.note.user.username} date: {self.note.created_at}"