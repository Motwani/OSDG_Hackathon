from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^give_feedback$', views.give_feedback, name='give_feedback'),
    url(r'^userhome/$',views.userhome, name='userhome'),
    url(r'^addprof$',views.addprof, name='addprof')
]