from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	calorieGoal = models.CharField(max_length=5)
	dietType = models.CharField(max_length = 15)
