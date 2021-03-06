"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from src.core import views as core_views

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('src.accounts.urls',  namespace='accounts')),
    url(r'^$', core_views.home, name='home'),
    url(r'^ebook-guia-de-compras-no-paraguai/$', core_views.home_guia, name='home_guia'),
    url(r'^ebook-guia-de-compras-no-paraguai/sucesso-inscricao/', core_views.sucesso_inscricao, name='sucesso_inscricao'),
    url(r'^ebook-guia-de-compras-no-paraguai/sem-permissao/', core_views.sem_permissao, name='sem_permissao'),
    url(r'^ebook-guia-de-compras-no-paraguai/guia-compras-paraguai.pdf', core_views.baixar_pdf, name='baixar_pdf'),
    url(r'^ebook-guia-de-compras-no-paraguai/cupons-compras-paraguai.pdf', core_views.baixar_cupons_pdf, name='baixar_cupons_pdf'),
    # url('', include('social_django.urls', namespace='social'))
]
