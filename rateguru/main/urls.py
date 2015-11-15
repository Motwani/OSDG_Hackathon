from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$',views.home,name='home'),
    url(r'^give_feedback$', views.give_feedback, name='give_feedback'),
    #url(r'^home/$',views.home, name='home')
    #url(r'^student_home$', views.student_home,name='student_home'),
    #url(r'^teacher_home$', views.teacher_home,name='teacher_home'),

    url(r'^userhome/$',views.userhome, name='userhome'),
    url(r'^addprof$',views.addprof, name='addprof')
]