from django.db import models


# Create your models here.
class UserDetails(models.Model):
	Name = models.CharField(max_length=100)
	District = models.CharField(max_length=200)
	Block = models.CharField(max_length=200)
	Panchayat = models.CharField(max_length=200)
	Email = models.CharField(max_length=100)
	Contact = models.DecimalField(max_digits = 11, decimal_places=0)
	
	def __str__(self):
		return self.Name
