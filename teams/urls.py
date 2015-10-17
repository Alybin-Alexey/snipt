from django.conf.urls import *
from teams import views


urlpatterns = \
    patterns('',
             url(r'^for-teams/$', views.for_teams),
             url(r'^for-teams/complete/$', views.for_teams_complete),
             url(r'^(?P<username>[^/]+)/members/$',
                 views.team_members,
                 name='team-members'))
