from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('cromongo.crm.urls')),
    
    url(r'^account/login/$', auth_views.login, { 'template_name':'login.html', }, name="auth_login"),
                                                                    
    url(r'^account/logout/$', auth_views.logout, { 'template_name':'logout.html'}, name="auth_logout"),
    url(r'^account/password/change/$', auth_views.password_change, {  }, name='auth_password_change'),
    url(r'^account/password/change/done/$', auth_views.password_change_done, {  }, name='auth_password_change_done'),
    url(r'^account/password/reset/$', auth_views.password_reset, {  }, name='auth_password_reset'),
    url(r'^account/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
                                                                auth_views.password_reset_confirm, 
                                                                {  },
                                                                name='auth_password_reset_confirm'),
    url(r'^account/password/reset/complete/$', auth_views.password_reset_complete, { }, name='auth_password_reset_complete'),
    url(r'^account/password/reset/done/$', auth_views.password_reset_done, {  }, name='auth_password_reset_done'),

    (r'^admin/', include(admin.site.urls)),
)
