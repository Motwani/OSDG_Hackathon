from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm
from .models import Feedback
# Create your views here.

def index(request):
    return render(request,'main/index.html',{'message':"Website is under construction!"})


def give_feedback(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			q1 = form.cleaned_data['q1']
			q2 = form.cleaned_data['q2']
			feed_obj = Feedback(choice1=q1,choice2=q2)
			feed_obj.save()
			return HttpResponse('Feedback Recieved.')
	else:
		form = FeedbackForm()
	return render(request,'main/give_feedback.html',{'form':form})
def student_home(request):
	user = User.objects.get(pk=request.user.id)
	return render(request,'main/student_home.html',{'user':user})

