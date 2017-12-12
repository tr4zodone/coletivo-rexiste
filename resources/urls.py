from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.link_list_view, name="resources"),
    url(r'^link/(?P<pk>\d+)$', views.LinkDetailView.as_view(), name='link_detail'),

    url(r'^link/new/$', views.NewLink.as_view(), name='add'),
    url(r'^link/(?P<pk>\d+)/edit/$', views.EditLink.as_view(), name='edit'),
    url(r'^link/(?P<pk>\d+)/delete/$', views.RemoveLink.as_view(), name='delete'),
    url(r'^new_tag/$', views.new_tag, name="new_tag"),
    ]
