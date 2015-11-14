from django.db import models
#from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator


class Prof(models.Model):
	prof_name = models.CharField(max_length=200)

class Rating(models.Model):
	prof_id = models.ForeignKey(Prof)
	clarity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	helpfullness = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	friendly = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	dedicated = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

class Student(models.Model):
	name = models.CharField(max_length=200)

class Comments(models.Model):
	prof_id = models.ForeignKey(Prof)
	description = models.CharField(max_length=200)
	helpfulness = models.IntegerField()

class Feedback(models.Model):
	 choice1 = models.IntegerField()
	 choice2 = models.IntegerField()

