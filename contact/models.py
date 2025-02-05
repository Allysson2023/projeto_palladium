from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Apartamento(models.Model):
    numero_apartamento = models.CharField(max_length=50)
    anda = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.numero_apartamento

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Carro(models.Model):
    nome_proprietario = models.CharField(max_length=254)
    placa = models.CharField(max_length=10)
    cor = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=50, blank=True)
    apartamento = models.ForeignKey(Apartamento, 
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True
                                     )
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')
    obs = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nome_proprietario

class Moradore(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField(max_length=245)
    cpf = models.CharField(max_length=25)
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')
    telefone = models.CharField(max_length=25)
    data_nascimento = models.CharField(max_length=12, blank=True)
    apartamento = models.ForeignKey(Apartamento, 
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True
                                     )
    email = models.EmailField(max_length=254, blank=True)
    obs = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nome

# Començando no index
class Registro_de_Visitante(models.Model):
    nome = models.CharField(max_length=245)
    cpf = models.CharField(max_length=25)
    telefone = models.CharField(max_length=25)
    data_registro = models.DateTimeField(default=timezone.now)
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')
    obs = models.TextField(blank=True)
 
    def __str__(self) -> str:
        return self.nome

class Registros_de_Entrega(models.Model):
    tipos_de_entrega = models.CharField(max_length=254)
    codigo_de_rastreamento = models.CharField(max_length=100, null=False,
                                                blank=True)
    destino = models.CharField(max_length=254)
    apartamento = models.ForeignKey(Apartamento, 
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True
                                     )
    data_registro = models.DateTimeField(default=timezone.now)
    obs = models.TextField(blank=True)
    foto_recebendo = models.ImageField(blank=True, 
                                       upload_to='pictures/%Y/%m/%d')
    foto_entrega = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')
    horario_da_entrega = models.DateTimeField(null=True,blank=True)
    quem_recebeu = models.CharField(max_length=150, blank=True)

    def __str__(self) -> str:
        return self.tipos_de_entrega

class Visitante(models.Model):
    nome = models.CharField(max_length=254)
    # telefone = models.CharField(max_length=20, blank=True)
    apartamento = models.ForeignKey(Apartamento,
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True
                                     )
    categoria = models.ForeignKey(Categoria, 
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True
                                     )
    autorizador = models.ForeignKey(User, on_delete=models.SET_NULL,
                                    blank=True, null=True
                                     )
    
    data_entrada = models.DateTimeField(default=timezone.now)
    id_registro = models.CharField(max_length=50)
    obs = models.TextField(blank=True)
    saida = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome

class Ocorrencia(models.Model):
    data = models.DateTimeField(default=timezone.now)
    nome_completo = models.CharField(max_length=254)
    
    ocorrencia = models.TextField()
    foto1 = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')
    foto2 = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                    blank=True, null=True)  # Campo owner que se relaciona ao usuário
    def __str__(self) -> str:
        return self.nome_completo

class Eventos(models.Model):
    local_evento = models.CharField(max_length=50)
    nome_responsavel = models.CharField(max_length=150)
    tipo_de_evento = models.CharField(max_length=100,  blank=True, null=True)
    apartamento = models.ForeignKey(Apartamento,
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True
                                     )
    data_horas_evento = models.DateTimeField(default=timezone.now)
    horario_final_evento = models.CharField(max_length=25)
    nomes_autorizados = models.TextField()
    veiculos_autorizados = models.TextField()
