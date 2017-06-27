from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload/$', views.upload),
    url(r'^edit/(?P<page_id>\w+)/$', views.edit),
    url(r'^pages/$', views.pages, name='pages'),
    url(r'^upload/uploadpage/$', views.uploadContent, name='uploadContent'),
    url(r'^edit/(?P<page_id>\w+)/images/$', views.uploadImages, name='uploadImages'),

]
