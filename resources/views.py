from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from resources.models import Link, Tag
from resources.forms import LinkBuild, TagBuild, LANGUAGE_CHOICES
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.
def link_list_view(request):

    links = Link.objects.all().order_by('title')
    tags = Tag.objects.all().filter(link__isnull=False).order_by("title").distinct()
       
    query = request.GET.get("q")

    if query:
        links = pt_links.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(language__icontains=query)
            ).distinct()

        tags = pt_links.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(language__icontains=query)
            ).distinct()

    return render(request, 'resources/resources_list.html', {'links':links, 'tags': tags})

# novo link
class NewLink(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'resources/link_form.html'
    success_url = reverse_lazy('resources')
    form_class = LinkBuild
    model = Link

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

# edit
class EditLink(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'resources/link_form.html'
    form_class = LinkBuild
    model = Link

