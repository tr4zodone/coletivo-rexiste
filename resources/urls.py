from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.link_list_view, name="resources"),
    url(r'^link/(?P<pk>\d+)$', views.LinkDetailView.as_view(), name='link_detail'),
    url(r'^file/(?P<pk>\d+)$', views.FileDetailView.as_view(), name='file_detail'),

    url(r'^link/new/$', views.NewLink.as_view(), name='add_link'),
    url(r'^file/new/$', views.NewFile.as_view(), name='add_file'),

    url(r'^link/edit/(?P<pk>\d+)/$', views.EditLink.as_view(), name='link_edit'),
    url(r'^file/edit/(?P<pk>\d+)/$', views.EditFile.as_view(), name='file_edit'),

    url(r'^link/delete/(?P<pk>\d+)/$', views.RemoveLink.as_view(), name='link_delete'),
    url(r'^file/delete/(?P<pk>\d+)/$', views.RemoveFile.as_view(), name='file_delete'),

    url(r'^new_tag/$', views.new_tag, name="new_tag"),
    ]


if settings.DEBUG:
    urlpatterns += [
       url(r'^media/(?P<path>.*)$', serve, {
           'document_root': settings.MEDIA_ROOT,
           }),
        ]
