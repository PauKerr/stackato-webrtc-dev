from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^file/(?P<file_id>[0-9a-zA-Z]+)/$',
        views.file, name='file'),
    url(r'^(?P<collection_id>[0-9]+)/$', views.collection, name='collection'),
]
