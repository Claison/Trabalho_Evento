from django.contrib import admin
from eventos.models import Pessoa,Autor,PessoaJuridica,PessoaFisica,Evento,EventoCientifico,ArtigoCientifico
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Autor)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)
