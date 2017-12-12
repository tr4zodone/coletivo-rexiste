from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^posts/$',views.post_list_view,name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contato/$', views.email, name='contato'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^rascunhos/$', views.rascunhos, name='rascunhos'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[-\w]+)/remover/$', views.Remover_Post.as_view(), name='remover'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[-\w]+)/publicar/$', views.publicar_post, name='publicar_post'),
    url(r'^post/new/$', views.NovoPost.as_view(), name='novo_post'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[-\w]+)/editar/$', views.AtualizarPost.as_view(), name='post_edit'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
