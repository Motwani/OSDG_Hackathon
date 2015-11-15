from django import forms


class FeedbackForm(forms.Form):
	MY_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
	q1 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label='Q1 text')
	q2 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label='Q2 text')

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

  