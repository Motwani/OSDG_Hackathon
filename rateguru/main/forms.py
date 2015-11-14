from django import forms


class FeedbackForm(forms.Form):
	#Options = (1,2,3,4,5)
	q1 = forms.IntegerField(required=True)
	q2 = forms.IntegerField(required=True)

