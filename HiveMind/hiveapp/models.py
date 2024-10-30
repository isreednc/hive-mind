from django.db import models

# max character in each string field
string_max = 200

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=string_max)

class Team(models.Model):
    team_id = models.BigAutoField(primary_key=True)
    users = models.ManyToManyField(User)

class Project(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=string_max)

