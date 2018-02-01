from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from resources.models import Link, Tag, File
from resources.forms import LinkBuild, TagBuild, FileUpload,LANGUAGE_CHOICES
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView
from django.urls import reverse_lazy
from itertools import chain
from operator import attrgetter as attr

# Create your views here.
def link_list_view(request):

    links = Link.objects.all().order_by('title')
    files = File.objects.all().order_by('title')

    link_tags = Tag.objects.all().filter(link__isnull=False).distinct()
    file_tags = Tag.objects.all().filter(file__isnull=False).distinct()

    tags_unsorted = list(chain(link_tags, file_tags))

    tags = sorted(set(tags_unsorted), key=attr('title'))

    query = request.GET.get("q")

    if query:
        files = pt_files.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(language__icontains=query)
            ).distinct()

        links = pt_links.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(language__icontains=query)
            ).distinct()

        tags = pt_tags.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(language__icontains=query)
            ).distinct()

    return render(request, 'resources/resources_list.html', {'links':links, 'tags': tags, 'files':files})

# novo link
class NewLink(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'resources/link_form.html'
    success_url = reverse_lazy('resources')
    form_class = LinkBuild
    model = Link

# enviar novo arquivo
class NewFile(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'resources/link_form.html'
    success_url = reverse_lazy('resources')
    form_class = FileUpload
    model = File

class FileDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'resources/file_detail.html'
    model = File

# página de cada link
class LinkDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'resources/link_detail.html'
    model = Link

# nova tag
def new_tag(request):
    tag_form = TagBuild()

    if request.method == 'POST':
        tag_form = TagBuild(request.POST)

        if tag_form.is_valid():
            title = tag_form.cleaned_data['title']
            tag_form.save()

            return HttpResponseRedirect('/resources/link/new/')

        else:
            tag_form = TagBuild()

    return render(request, "resources/new_tag.html", {'tag_form': tag_form})

# remove
class RemoveLink(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('resources')

class RemoveFile(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('resources')

# edit
class EditLink(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'resources/link_form.html'
    form_class = LinkBuild
    success_url = reverse_lazy('resources')
    model = Link

class EditFile(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'resources/link_form.html'
    form_class = FileUpload
    success_url = reverse_lazy('resources')
    model = File

