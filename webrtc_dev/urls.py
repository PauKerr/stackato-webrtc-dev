from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^log/', include('logs.urls', namespace='logs')),
    # Examples:
    # url(r'^$', 'stackato.views.home', name='home'),
    # url(r'^stackato/', include('stackato.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL + 'logs/', document_root='logs/static/logs/')

