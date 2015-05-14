from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
import redapp, django.contrib.auth.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^redapp/', include('redapp.urls')),
    url(r'^$', redapp.views.index, name='index'),
    url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'login.html'}),
    url(r'^index/$', redapp.views.index, name='index'),
    url(r'^logout/$', redapp.views.user_logout, name='user_Logout'),
    url(r'^r/(?P<inputSubreddit>[\w-]+)/$', redapp.views.getSubreddit, name='getSubreddit'),
    url(r'^r/(?P<inputSubreddit>[\w-]+)/(?P<nextp>[\w-]+)/$', redapp.views.getSubreddit, name='getSubreddit'),
    url(r'^u/(?P<inputRedditor>[\w-]+)/$', redapp.views.getRedditor, name='getRedditor'),
    url(r'^u/(?P<inputRedditor>[\w-]+)/(?P<nextp>[\w-]+)/$', redapp.views.getRedditor, name='getRedditor'),
    url(r'^fav/(?P<inputRedditor>[\w-]+)/(?P<inputImage>[\w-]+)/$', redapp.views.add_fav, name='add_fav'),
    url(r'^favorites/$', redapp.views.getFavorites, name='getFavorites'),
    )

