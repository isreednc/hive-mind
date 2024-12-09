from django.db import models
from django.contrib.auth.models import User, Group
# from ..tasks.models import Note


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
    # notes = models.ManyToManyField(Note, related_name="timeline_nodes")  # Add relationship with Note

    def mark_completed(self):
        self.is_complete = True
        self.save()

    def get_notes(self):
        """Retrieve related notes."""
        return self.notes.all()

    def __str__(self):
        return self.title

    # title = models.CharField(max_length=100)
    # description = models.TextField()
    # due_date = models.DateField()

    # class Meta:
    #     proxy = True

    # def due_date(self):
    #     return self.created_at


