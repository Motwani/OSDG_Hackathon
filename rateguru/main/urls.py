from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$',views.home,name='home'),
    url(r'^give_feedback$', views.give_feedback, name='give_feedback'),
    url(r'^addprof$',views.addprof, name='addprof'),
    url(r'^addcourse$',views.addcourse,name='addcourse'),
    url(r'^prof_detail/(?P<prid>[0-9]+)/$',views.prof_detail,name='prof_detail'),
    url(r'^add_course$',views.add_course,name='add_course'),
    url(r'^subscribe/(?P<cid>[0-9]+)/$',views.subscribe,name='subscribe'),
    url(r'^student_detail/(?P<stid>[0-9]+)/$',views.student_detail,name='student_detail'),
]
