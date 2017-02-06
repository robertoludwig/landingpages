from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from src.core.models import *



class UsuarioGuiaForm(ModelForm):
    class Meta:
        model = UsuarioGuia
        exclude = ['ativo']

    assuntos = forms.ModelMultipleChoiceField(
            queryset=AssuntoSaberMais.objects.filter(ativo=True),
            widget=forms.CheckboxSelectMultiple(),
            required=False
    )

    quais_assuntos = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Quais?'})
    )

    def __init__(self, *args, **kwargs):
        super(UsuarioGuiaForm, self).__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({
            'class': 'form-control required',
            'placeholder': 'Nome Completo'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control required',
            'placeholder': 'Endereço de e-mail'
        })

        self.fields['cidade'].widget.attrs.update({
            'class': 'form-control required',
            'placeholder': 'Cidade'
        })

        self.fields['ja_fez_compras'].widget.attrs.update({
            'class': 'form-control required'
        })

        self.fields['assuntos'].widget.attrs.update({
            'class': 'required'
        })

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        words = [w.capitalize() for w in nome.split()]
        return ' '.join(words)

    def clean(self):
        if not self.cleaned_data.get('nome'):
            raise ValidationError('Informe seu nome')

        return self.cleaned_data