from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=150,null=True)

    def __str__(self):
        return "%s"%self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Autor(Pessoa):
    curriculo = models.TextField()
    artigos = []
    def __str__(sef):
        return super(Pessoa,self).__str__()

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class PessoaJuridica(Pessoa):
    cnpj = models.CharField("CNPJ",max_length=14)
    razaoSocial = models.CharField("Razão social",max_length=100,null=True)
    
    def __str__(sef):
        return super(Pessoa,self).__str__() + "%s"%self.cnpj
    
    class Meta:
        verbose_name = "Pessoa jurídica"
        verbose_name_plural = "Pessoas jurídicas"

class PessoaFisica(Pessoa):
    cpf = models.CharField("CPF",max_length=14)
    
    def __str__(sef):
        return super(Pessoa,self).__str__() + "%s"%self.cpf

    class Meta:
        verbose_name = "Pessoa física"
        verbose_name_plural = "Pessoas físicas"

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    eventoPrincipal = models.CharField("Evento principal",max_length=100,null=True)
    sigla = models.CharField(max_length=2,null=True)
    dataEHoraDeInicio = models.DateTime("Data e hora de início",null=True)
    palavraChave = models.CharField("Palavra chave",max_length=100,null=True)
    logoTipo = models.CharField("Logo tipo",max_length=150,null=True)
    realizador = models.ForeignKey(Pessoa,related_name="evento")
    cidade = models.CharField(max_length=100,null=True)
    uf - models.CharField(max_length=2,null=True)
    endereco = models.CharField("Endereço",max_length=100,null=True)
    cep = models.CharField("CEP",max_length=8,null=True)


    def __str__(self):
        return "%s"%self.nome

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


class EventoCientifico(Evento):
    issn = models.CharField("ISSN",max_length=100)

    def __str__(self):
        return super(self).__str__() + "%s"%self.issn
    
    class Meta:
        verbose_name = "Evento científico"
        verbose_name_plural = "Eventos científicos"

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=100)
    autores = []
    evento = models.ForeignKey(EventoCientifico,related_name="artigoCientifico",blank=True)

    def __str__(self):
        return "%s"%self.titulo

    class Meta:
        verbose_name = "Artigo científico"
        verbose_name_plural = "Artigos científicos"