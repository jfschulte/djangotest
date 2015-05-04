from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
import rango

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^r/(?P<inputSubreddit>[\w-]+)/$', rango.views.getSubreddit, name='getSubreddit'),
    url(r'^r/(?P<inputSubreddit>[\w-]+)/(?P<nextp>[\w-]+)/$', rango.views.getSubreddit, name='getSubreddit'),
    url(r'^u/(?P<inputRedditor>[\w-]+)/$', rango.views.getRedditor, name='getRedditor'),
    url(r'^u/(?P<inputRedditor>[\w-]+)/(?P<nextp>[\w-]+)/$', rango.views.getRedditor, name='getRedditor'),
    url(r'^fav/(?P<inputRedditor>[\w-]+)/(?P<inputImage>[\w-]+)/$', rango.views.add_fav, name='add_fav'),
    url(r'^favfav/$', rango.views.getFavorites, name='getFavorites'),
    )

