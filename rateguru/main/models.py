from django.db import models
from django.forms import ModelForm

# Create your models here.
class Prof(models.Model):
	prof_name = models.Charfield(max_length=200)

class Rating(models.Model):
	prof_id = models.Foriegnkey(Prof)
	clarity = models.integer(max_value=5,min_value=1)
	helpfullness = models.integer(max_value=5,min_value=1)
	friendly = models.integer(max_value=5,min_value=1)
	dedicated = models.integer(max_value=5,min_value=1)

class Student(models.Model):
	name = models.Chartext(max_length=200)

class Comments(models.Model):
	prof_id = models.Foriegnkey(Prof)
	description = models.Text()
	helpfulness = models.integer()

class FeedbackForm(ModelForm):
	 name = forms.CharField(max_length=100)
	 title = forms.CharField(max_length=3,widget=forms.Select(choices=TITLE_CHOICES))
	 birth_date = forms.DateField(required=False)



