import os

import requests
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
        usuario = UsuarioGuia.objects.get(email=form.cleaned_data['email'])
    except ObjectDoesNotExist:
        usuario = False

    if usuario:
        usuario.nome = form.cleaned_data['nome']
        if not usuario.ativo:
            usuario.ativo = True
        usuario.save()
    else:
        usuario = form.save()

    url_action = 'http://www.comprasparaguai.com.br/newsletter/clique/?campanha=inscreveu_LP_ebook_guia_compras_vantagens&origem=landing-page&email=' + usuario.email
    request_url(url_action)

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

    file_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'src/core/static/guia/file/cupons-lojas-Paraguai.pdf')

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404

def sem_permissao(request):
    return render(request, 'guia/sem-permissao.html')

def request_url(urlData):
    import urllib
    from requests.exceptions import HTTPError

    try:
        r = requests.get(urlData)
        r.raise_for_status()
    except HTTPError:
        pass
    else:
        webURL = urllib.request.urlopen(urlData)
        webURL.read()

    # import pdb
    # pdb.set_trace()

