from django import forms


class FeedbackForm(forms.Form):
	MY_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
	q1 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label='Q1 text')
	q2 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label='Q2 text')


class AddProfForm(forms.Form):
	prof_name = forms.CharField(max_length=200)
	clarity = forms.FloatField()
	helpfullness = forms.FloatField()
	friendly = forms.FloatField()
	dedicated = forms.FloatField()
	noofratings = forms.IntegerField()
  