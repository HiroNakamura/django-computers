from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^computadoras/(?P<pk>[0-9]+)/$', views.comp_detalle, name='comp_detalle'),
    url(r'^computadoras/nueva/$', views.comp_nueva, name='comp_nueva'),
    url(r'^computadoras/usuarios', views.usuarios_list, name='usuarios_list'),
    url(r'^computadoras/usuario/(?P<pk>[0-9]+)/$', views.usuario_detalle, name='usuario_detalle'),
    url(r'^computadoras/nuevo/$', views.usuario_nuevo, name='usuario_nuevo'),
]
