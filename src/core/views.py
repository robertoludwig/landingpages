from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from src.core.forms import UsuarioGuiaForm
from django.core.urlresolvers import reverse
from src.core.models import UsuarioGuia


def home(request):
    if request.method == 'POST':
        return cria_form_guia(request)

    return form_vazio_guia(request)

def form_vazio_guia(request):
    return render(request,'core/index.html', {'form': UsuarioGuiaForm()})

def cria_form_guia(request):
    form = UsuarioGuiaForm(request.POST)
    if not form.is_valid():
        return render(request,'core/index.html', {'form': form})

    try:
        existe = UsuarioGuia.objects.get(email=form.cleaned_data['email'])
    except ObjectDoesNotExist:
        existe = False

    if existe:
        existe.nome = form.cleaned_data['nome']
        if not existe.ativo:
            existe.ativo = True
        existe.save()
    else:
        form.save()

    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect(reverse('home'))

