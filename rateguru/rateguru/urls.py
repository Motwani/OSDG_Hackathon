from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rateguru.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main/', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login' , 'django_cas.views.login'),
    url(r'^accounts/logout' ,'django_cas.views.logout'),
)
