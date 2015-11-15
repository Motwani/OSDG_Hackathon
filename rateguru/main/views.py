from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm,AddProfForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Feedback
from django.http import HttpResponseRedirect
from .models import Feedback,Prof
# Create your views here.

def index(request):
	user = User.objects.get(pk=request.user.id)
	print user.username
	return render(request,'main/index.html',{'message':"Website is under construction!",'user' : user})
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

@login_required(login_url='accounts/login')
def home(request):
	user = User.objects.get(pk=request.user.id)
	list = ['students','research']
	if any(word in user.username for word in list):
		#return HttpResponseRedirect('student_home',username=user.username) 
		return render(request,'main/student_home.html',{'user':user})
	else:
		#return HttpResponseRedirect('teacher_home', username=user.username) 
		return render(request,'main/teacher_home.html',{'user':user})

def teacher_home(request):
	teach = Prof.objects.get(pk=1)
	print teach.name
	return render(request,'main/teacher_home.html',{'user':user})

def userhome(request):
	all_prof = Prof.objects.all()
	return render(request,'main/userhome.html',{'all_prof':all_prof})

def addprof(request):
	if request.method == 'POST':
		form = AddProfForm(request.POST)
		if form.is_valid():
			prof_name = form.cleaned_data['prof_name']
			clarity = form.cleaned_data['clarity']
			helpfullness = form.cleaned_data['helpfullness']
			friendly = form.cleaned_data['friendly']
			dedicated = form.cleaned_data['dedicated']
			noofratings = form.cleaned_data['noofratings']
			prof_obj = Prof(prof_name=prof_name,
				clarity=clarity,
				helpfullness=helpfullness,
				friendly=friendly,
				dedicated=dedicated,
				noofratings=noofratings,
				)
			prof_obj.save()
			return HttpResponse('Prof Created')
	else:
		form = AddProfForm()
	return render(request,'main/addprof.html',{'form':form})

#def prof_profile(request):