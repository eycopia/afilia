from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'main.views.index'),
    (r'^index/$', 'main.views.index'),

    (r'^accounts/login/$', login, {'template_name':'login.html'}),
    (r'^accounts/loguot/$', logout),
    (r'^accounts/profile/$', 'main.views.redirec_profile'),
    (r'^nuevo-afiliado/$', 'afiliado.views.add_afiliado'),
    (r'^ubigeo/$','ubigeo.views.search_ubigeo'),
)
