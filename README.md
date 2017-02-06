# Projeto Base

Projeto Base

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virutalenv com o Python 3.5
3. Ative o Virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Migre seus modelos para o Banco de Dados
7. Roda o collectstatic para configurar arquivos staticos
8. Execute os testes.

```console
git clone https://github.com/tyagow/django-base.git Nome-Do-Projeto
cd 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py collectstatic
python manage.py migrate
python manage.py test
python manage.py runserver
```
## Configurar Social Auth

https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html
Configurar variaveis no .env
SOCIAL_AUTH_TWITTER_KEY=
SOCIAL_AUTH_TWITTER_SECRET=
SOCIAL_AUTH_FACEBOOK_KEY=
SOCIAL_AUTH_FACEBOOK_SECRET=

## Como fazer primeiro deploy ?

1. Install Digital Ocean Dokku image
2. Send your ssh-key to dokku
3. Connect via ssh to your server
4. Create app in dokku 
5. Install postgres plugin in dokku 
6. Create database for your app in dokku
7. Link database and app in dokku
8. Set DEBUG in dokku 
9. Generate new SECRET_KEY
10. Set SECRET_KEY in dokku
11. Set ALLOWED_HOSTS in dokku
12. Set Global Domain dor dokku
13. Push your code to dokku

```console
(local) cat ~/.ssh/id_rsa.pub | ssh root@<your.ip.address> "sudo sshcommand acl-add dokku [description]"
(local) ssh root@<your.ip.address>
(server) dokku apps:create <app-name>
(server) sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git
(server) dokku postgres:create <database-name>
(server) dokku postgres:link <databse-name> <app-name>
(local) git remote add dokku dokku@dokku.me:<app-name>
(local) ssh dokku@<your.ip.address> config:set <app-name> DEBUG=False
(local) python contrib/secret_gen.py
(local) ssh dokku@<your.ip.address> config:set <app-name> SECRET_KEY='<new-generated-key>'
(local) ssh dokku@<your.ip.address> config:set <app-name> ALLOWED_HOSTS=<app-name>.<your.ip.address>.xip.io
(local) ssh dokku@<your.ip.address> domains:add-global <your.ip.address>.xip.io
(local) git push dokku master
```
**NOTES**
* Depois do primeiro deploy feito basta um comando para o deploy:
`git push dokku master`
* Não esquecer de migrar/atualizar o banco de dados sempre que alterar um modelo:
`ssh dokku@<your.ip.address> run <app-name> python manage.py migrate`

## Features

* Django 1.10.5
* Bootstrap 3.3.7
* JQuery 3.1.1
* Python Decouple
* DJ Static (serving static files locally)
* Dj Database URL 
* Django test without migrations
* Django Crispy Forms
* Basic User Login App
* Django Extensions
* Dokku pre configured
