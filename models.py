from django.db import models
from datetime import datetime

# Create your models here.
class train(models.Model):
	slNo = models.IntegerField()
	Date =  models.DateField()
	TrainName = models.CharField(max_length = 50)
	DepartureFrom = models.CharField(max_length = 50)
	Departuretime =models.TimeField()
	Departuretime =models.TimeField()
	ArrivingAt = models.CharField(max_length = 50)
	Arrivaltime =models.TimeField()
	class Meta:
			   db_table = "train"