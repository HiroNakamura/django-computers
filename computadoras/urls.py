from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^departamentos/', views.dept_list, name='dept_list'),
    url(r'^computadoras/', views.comp_list, name='comp_list'),
]