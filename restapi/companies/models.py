from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	openPrice = models.FloatField()
	closePrice = models.FloatField()
	volume = models.IntegerField()

	def __str__(self):
		return self.ticker


