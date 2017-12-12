from django import forms
from resources.models import Link, LANGUAGE_CHOICES, Tag

class LinkBuild(forms.ModelForm):
    title = forms.CharField(required=True, label="Título")
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, widget=forms.Select(), label="Idioma")  

    class Meta():
        model = Link
        fields = ('title', 'language', 'tag', 'url') 

class TagBuild(forms.ModelForm):
    title = forms.CharField(required=True, label="Nome da tag")

    class Meta():
        model = Tag
        fields=('title',)
