from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('cromongo.crm.urls')),

    (r'^admin/', include(admin.site.urls)),
)
