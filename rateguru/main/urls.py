from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$',views.home,name='home'),
    url(r'^give_feedback$', views.give_feedback, name='give_feedback'),
    #url(r'^home/$',views.home, name='home')
    #url(r'^student_home$', views.student_home,name='student_home'),
    url(r'^teacher_home/$', views.teacher_home,name='teacher_home'),

    url(r'^userhome/$',views.userhome, name='userhome'),
    url(r'^addprof$',views.addprof, name='addprof'),
    url(r'^addcourse$',views.addcourse,name='addcourse'),
    url(r'^/prof_detail/(?P<prof_id>[0-9]+)/$',views.prof_detail,name='prof_detail'),
]
