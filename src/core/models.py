from django.db import models


class AssuntoSaberMais(models.Model):
    nome = models.CharField('assunto', max_length=45, null=False, blank=False)
    ordem = models.IntegerField('ordem', default=99)
    ativo = models.BooleanField('disponível', default=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'assuntos saber mais'
        verbose_name = 'assunto saber mais'
        ordering = ('ordem',)

    def __str__(self):
        return self.nome


class UsuarioGuia(models.Model):
    CHOICES_FEZ_COMPRAS = (
        (True, 'Sim'),
        (False, 'Não'),
    )

    nome = models.CharField('nome', max_length=45, null=False, blank=False)
    email = models.EmailField('e-mail', max_length=45, null=False, blank=False)
    cidade = models.CharField('cidade', max_length=45, null=False, blank=False)
    ja_fez_compras = models.BooleanField('já fez compras no Paraguai?', choices=CHOICES_FEZ_COMPRAS)
    assuntos = models.ManyToManyField(AssuntoSaberMais, blank=True)
    quais_assuntos = models.CharField('quais assuntos?', max_length=250, null=True, blank=True) #quando selecionar 'Outros'
    ativo = models.BooleanField('disponível', default=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'usuários guia'
        verbose_name = 'usuário guia'
        ordering = ('-id',)

    def __str__(self):
        return self.nome
