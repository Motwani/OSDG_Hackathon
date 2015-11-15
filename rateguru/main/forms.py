from django import forms
from .models import PQuestion

class FeedbackForm(forms.Form):
	MY_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
	P=PQuestion.objects.all()
	arr=[]
	for i in P:
		arr.append(i.question_text)
	q1 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label=arr[0])
	q2 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label=arr[1])
	q3 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label=arr[2])
	q4 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label=arr[3])

class RatingForm(forms.Form):
	MY_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
	clarity = forms.ChoiceField(widget=forms.RadioSelect,choices=MY_CHOICES,required=True)
	friendly = forms.ChoiceField(widget=forms.RadioSelect,choices=MY_CHOICES,required=True)
	helpfullness = forms.ChoiceField(widget=forms.RadioSelect,choices=MY_CHOICES,required=True)
	dedicated = forms.ChoiceField(widget=forms.RadioSelect,choices=MY_CHOICES,required=True)


class AddProfForm(forms.Form):
	prof_name = forms.CharField(max_length=200)
	clarity = forms.FloatField()
	helpfullness = forms.FloatField()
	friendly = forms.FloatField()
	dedicated = forms.FloatField()
	noofratings = forms.IntegerField()

class AddCourseForm(forms.Form):
	Name = forms.CharField(max_length=20)
	semester = forms.IntegerField()
class AddPquestionForm(forms.Form):
	question_text = forms.CharField(max_length=100)

  