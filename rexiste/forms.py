from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from rexiste.models import Post

class ContactForm(forms.Form):
    nome = forms.CharField(required=True)
    email= forms.EmailField(required=True)
    assunto= forms.CharField(required=True)
    mensagem= forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):

    cover = forms.ImageField(required=True)
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta():
        model = Post
        fields = ('author', 'title', 'cover', 'text')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'postcontent'})
            }
