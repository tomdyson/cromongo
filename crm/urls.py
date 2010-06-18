#URLconf for cromongo.crm

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

    #basic views
    url(r'^',  'crm.views.core.home', { }, name="crm_views_core_home"),
    url(r'^person/(?P<person_id>[0-9a-z_-]+)/$',  'crm.views.core.person_details', { }, name="crm_views_core_person_details"),
    
)