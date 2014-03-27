from django.db import models

# Create your models here.
class Title(models.Model):
	owner = models.TextField()
	
	