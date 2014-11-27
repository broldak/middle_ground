from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
	user = models.OneToOneField(User)

	website = models.URLField(blank=True)
	
	def __str__(self):
		return self.user.username
