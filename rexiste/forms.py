from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from rexiste.models import Post

from ckeditor_uploader.fields import RichTextUploadingField

class ContactForm(forms.Form):
    nome = forms.CharField(required=True)
    email= forms.EmailField(required=True)
    assunto= forms.CharField(required=True)
    mensagem= forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):

    cover = forms.ImageField(required=True)
    forms = RichTextUploadingField()

    class Meta():
        model = Post
        fields = ('author', 'title', 'cover', 'text')