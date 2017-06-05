from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about/', views.about, name='about'),
    url(r'^services/', views.services, name='services'),
    url(r'^index/', views.index, name='index'),

]

