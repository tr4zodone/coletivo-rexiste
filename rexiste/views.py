from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rexiste.models import Post
from django.db.models import Q
from rexiste.forms import PostForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from hitcount.views import HitCountDetailView

from django.conf import settings

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'rexiste/about.html'

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome'] 
            assunto = form.cleaned_data['assunto']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            relay= '''Enviado por: %s\n via %s
            Assunto: %s\n
            Mensagem: 
            %s
            '''%(nome, email, assunto, mensagem) 
            try:
                send_mail(assunto, relay, settings.EMAIL_HOST_USER, ['rexistircoletivo@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "rexiste/contato.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')

def post_list_view(request):
    
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts_sorted = posts.order_by('-hit_count_generic__hits')[:9]

    query = request.GET.get("q")
    page = request.GET.get('page')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
            ).distinct()
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1) 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'rexiste/post_list.html', {'posts':posts, 'posts_sorted': posts_sorted})
 
class PostDetailView(HitCountDetailView):
    model = Post
    slug_field = "title"
    count_hit = True

class NovoPost(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'rexiste/post_detail.html'
    form_class = PostForm
    model = Post

class AtualizarPost(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'rexiste/post_detail.html'
    form_class = PostForm
    model = Post

@login_required
def rascunhos(request):
    posts = Post.objects.all().filter(published_date__isnull=True).order_by('create_date')

    query = request.GET.get("q")
    page = request.GET.get('page')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
            ).distinct()

    paginator = Paginator(posts, 25)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1) 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'rexiste/rascunhos.html', {'posts':posts})

class Remover_Post(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

######## login-required zone #########

@login_required
def publicar_post(request, slug, pk):
    post = get_object_or_404(Post, slug=slug, pk=pk)
    post.publish()
    return redirect('post_detail', slug=slug, pk=pk)

