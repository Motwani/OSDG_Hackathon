from django import forms


class FeedbackForm(forms.Form):
	MY_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
	q1 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label='Q1 text')
	q2 = forms.ChoiceField(widget=forms.RadioSelect, choices=MY_CHOICES,required=True, label='Q2 text')
  