from django.conf.urls.defaults import *

from snipts import views


urlpatterns = patterns('',
    url(r'^$',                                             views.home,        name='home'),
    url(r'^public/$',                                      views.list_public, name='list-public'),
    url(r'^public/tag/(?P<tag_slug>[^/]+)/$',              views.list_public, name='list-public-tag'),
    url(r'^(?P<username>[^/]+)/$',                         views.list_user,   name='list-user'),
    url(r'^(?P<username>[^/]+)/tag/(?P<tag_slug>[^/]+)/$', views.list_user,   name='list-user-tag'),
    url(r'^(?P<username>[^/]+)/(?P<snipt_slug>[^/]+)/$',   views.detail,      name='detail'),
)
