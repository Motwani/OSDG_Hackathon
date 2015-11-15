from django.db import models
#from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Courses(models.Model):
	Name = models.CharField(max_length=20)
	semester = models.IntegerField()

class Prof(models.Model):
	prof_name = models.CharField(max_length=200)
	clarity = models.FloatField()
	helpfullness = models.FloatField()
	friendly = models.FloatField()
	dedicated = models.FloatField()
	noofratings = models.IntegerField()
	courses = models.ManyToManyField(Courses)

class Rating(models.Model):
	prof_id = models.ForeignKey(Prof)
	clarity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	helpfullness = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	friendly = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	dedicated = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

class Student(models.Model):
	name = models.CharField(max_length=200)
	courses = models.ManyToManyField(Courses)


class Comments(models.Model):
	prof_id = models.ForeignKey(Prof)
	description = models.CharField(max_length=200)
	helpfulness = models.IntegerField()


class Feedback(models.Model):
	choice1 = models.IntegerField()
	choice2 = models.IntegerField()

#class FeedbackForm(ModelForm):
#	 name = forms.CharField(max_length=100)
#	 title = forms.CharField(max_length=3,widget=forms.Select(choices=TITLE_CHOICES))
#	 birth_date = forms.DateField(required=False)


