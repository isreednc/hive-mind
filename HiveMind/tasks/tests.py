from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note, Reply

# Create your tests here.
class NoteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="john",
            password="password"
        )
        
        self.note = Note.objects.create(
            content="Testing note functionality",
            user = self.user
        )
    
    def test_note(self):
        self.assertEqual(self.user.username, "john")
        self.assertEqual(self.note.content, "Testing note functionality")

    def test_note_string(self):
        self.assertEqual(str(self.note), "john")

    def test_mark_complete(self):
        self.note.mark_completed()
        self.assertTrue(self.note.is_complete)
    