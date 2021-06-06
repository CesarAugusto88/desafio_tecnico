# coding:utf-8
from django.forms import ModelForm, TextInput, URLField
from . import models


class EncurtarURLForm(ModelForm):
    url = URLField(widget=TextInput(attrs={
        'placeholder': 'Entre com a URL que deseja encurtar...',
    }))

    class Meta:
        model = models.Link
        fields = ['usuario']