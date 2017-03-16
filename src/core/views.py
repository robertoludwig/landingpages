import os

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from src import settings
from src.core.forms import UsuarioGuiaForm
from django.core.urlresolvers import reverse
from src.core.models import UsuarioGuia


def home(request):
    return render(request, 'core/index.html', locals())

def home_guia(request):
    if request.method == 'POST':
        return cria_form_guia(request)
    return form_vazio_guia(request)

def form_vazio_guia(request):
    return render(request, 'guia/index.html', {'form': UsuarioGuiaForm()})

def cria_form_guia(request):
    form = UsuarioGuiaForm(request.POST)
    if not form.is_valid():
        return render(request, 'guia/index.html', {'form': form})

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

    #cria a sessao para baixar o app
    request.session['inscricao_guia'] = True

    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect(reverse('sucesso_inscricao'))

def sucesso_inscricao(request):
    if not 'inscricao_guia' in request.session:
        return HttpResponseRedirect(reverse('sem_permissao'))
    return render(request, 'guia/sucesso-inscricao.html')

def baixar_pdf(request):
    if not 'inscricao_guia' in request.session:
        return HttpResponseRedirect(reverse('sem_permissao'))

    file_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'src/core/static/guia/file/guia-compras-paraguai.pdf')

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404

def baixar_cupons_pdf(request):
    if not 'inscricao_guia' in request.session:
        return HttpResponseRedirect(reverse('sem_permissao'))

    file_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'src/core/static/guia/file/guia-compras-paraguai.pdf')

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404

def sem_permissao(request):
    return render(request, 'guia/sem-permissao.html')

