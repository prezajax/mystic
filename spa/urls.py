from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about/', views.about, name='about'),
    url(r'^peels/', views.peels, name='peels'),
    url(r'^index/', views.index, name='index'),
    url(r'^led/', views.led, name='led'),
     url(r'^oxygen/', views.oxygen, name='oxygen'),

]

