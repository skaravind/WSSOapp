from django.db import models


# Create your models here.
class User(models.Model):
	Name = models.CharField(max_length=100)
	District = models.CharField(max_length=200)
	Email = models.CharField(max_length=100)
	contact = models.DecimalField(max_digits = 11, decimal_places=0)
	
	def __str__(self):
		return self.name
