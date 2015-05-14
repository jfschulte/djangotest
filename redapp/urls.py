from django.conf.urls import patterns, url
from redapp import views
import django.contrib.auth.views, django.contrib.auth.urls

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^r/(?P<inputSubreddit>[\w-]+)/$', views.getSubreddit, name='getSubreddit'),
    url(r'^r/(?P<inputSubreddit>[\w-]+)/(?P<nextp>[\w-]+)/$', views.getSubreddit, name='getSubreddit'),
    url(r'^u/(?P<inputRedditor>[\w-]+)/$', views.getRedditor, name='getRedditor'),
    url(r'^u/(?P<inputRedditor>[\w-]+)/(?P<nextp>[\w-]+)/$', views.getRedditor, name='getRedditor'),

    )
