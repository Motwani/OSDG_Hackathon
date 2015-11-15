from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm,AddProfForm,AddCourseForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Feedback
from django.http import HttpResponseRedirect
from .models import Feedback,Prof,Courses,Student
from django.core.urlresolvers import reverse
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
		num = Student.objects.filter(email = user.username).count()
		if num==0:
			a = user.username.split('@')
			prof_obj = Student(name=a[0],email=user.username)
			prof_obj.save()
		prof = Student.objects.get(email=user.username)
		return HttpResponseRedirect(reverse('main:student_detail', args=(prof.id,)))
	else:
		num = Prof.objects.filter(email = user.username).count()
		if num==0:
			a = user.username.split('@')
			prof_obj = Prof(prof_name=a[0],email=user.username)
			prof_obj.save()
		prof = Prof.objects.get(email=user.username)
		return HttpResponseRedirect(reverse('main:prof_detail', args=(prof.id,)))

def prof_detail(request,prid):
	prof = Prof.objects.get(pk=prid)
	return render(request,'main/prof_detail.html',{'prof':prof})

def student_detail(request,stid):
	student = Student.objects.get(pk=stid)
	return render(request,'main/student_detail.html',{'student':student})


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
def addcourse(request):
	if request.method == 'POST':
		form = AddCourseForm(request.POST)
		if form.is_valid():
			Course_name = form.cleaned_data['Name']
			semester = form.cleaned_data['semester']
			Course_obj = Courses(Name=Course_name,
						semester=semester,
				)
			Course_obj.save()
			return HttpResponse('Course Created')
	else:
		form = AddCourseForm()
	return render(request,'main/addcourse.html',{'form':form})


#def prof_profile(request):