from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class VisitantesForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Escreva nome do Visitante',
            }
        ),
        help_text='Escreva nome do Visitante',
    )
    obs = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.Textarea(
            attrs={
                'placeholder': 'observação, esta deixando veiculo ou moto aonde? caso esteja entrando junto...' 
                
            }
        )
    )
    id_registro = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite o numero do Registro do Visitante',
            }
        ),
        help_text='Registro do Visitante',
    )
    saida = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',  # Exibe o calendário com horário
                'class': 'form-control',
                'placeholder':'Coloque a data de saida'
            }
        ),
        required=False, help_text='Ao Click no campo selecione a data e o horario'
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = models.Visitante
        fields = (
            'nome', 'apartamento', 'categoria', 'autorizador', 'data_entrada',
            'id_registro', 'obs', 'saida',
        )
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome == 'ABC':
            self.add_error(
            'nome',
            ValidationError('Não pode escreve ABC',
                            code='Invalid'
                            )
            )
        return nome
    
class Registro_visitantesForm(forms.ModelForm):
    nome = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nome Completo do Visitante...',
            }
        )
    )
    cpf = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.TextInput(
            attrs={
                'placeholder':'numero do CPF, RG ou algum documento',
            }
        )
    )
    telefone = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ex: (00) 0 00000000',
            }
        )
    )
    obs = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.Textarea(
            attrs={
                'placeholder':'Escreva observação do Registro',
            }
        )
    )
    foto = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        ), help_text='Foto do Visitante'
    )
    class Meta:
        model = models.Registro_de_Visitante
        fields = (
            'nome', 'cpf', 'telefone',
            'obs', 'foto',
        )

class Registros_de_EntregaForm(forms.ModelForm):

    tipos_de_entrega = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nome da entrega...',
            }
        )
    )
    codigo_de_rastreamento = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.TextInput(
            attrs={
                'placeholder':'Caso tenha...',
            }
        )
    )

    destino = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nome do Proprietario...',
            }
        )
    )
    obs = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.Textarea(
            attrs={
                'placeholder':'Escreva observação ser tiver Danificado ou qualquer ocorrencia na hora do recebimento ou da entrega...',
            }
        )
    )

    saida = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',  # Exibe o calendário com horário
                'class': 'form-control',
                'placeholder':'Coloque a data de saida'
            }
        ),
        required=False, help_text='Ao Click no campo selecione a data e o horario'
    )
    foto_recebendo= forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    foto_entrega = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        ),
        required=False,
    )
    
    quem_recebeu = forms.CharField(
        required=False,  # Torna o campo opcional
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nome de quem Recebeu a Entrega...',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = models.Registros_de_Entrega
        fields = (
            'tipos_de_entrega', 'codigo_de_rastreamento', 'destino',
            'apartamento', 'data_registro', 'obs','foto_recebendo', 
            'foto_entrega', 
            'quem_recebeu',
        )

class OcorrenciaForm(forms.ModelForm):

    nome_completo = forms.CharField(
        required=True,  # Torna o campo opcional
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nome completo do Ronda ou Porteiro...',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = models.Ocorrencia
        fields = (
            'data', 'nome_completo', 'ocorrencia', 
        )



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )
        return email

class EventosForm(forms.ModelForm):
    local_evento = forms.CharField(
        label='Local do Evento',
        min_length=2,
        max_length=85,
        required=True,
        help_text='Digite o nome do Local.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    nome_responsavel = forms.CharField(
        label='Nome do Responsavel do Evento',
        min_length=2,
        max_length=85,
        required=True,
        help_text='Responsavel',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    tipo_de_evento = forms.CharField(
        label='Que Tipo de Evento vai ser?',
        min_length=2,
        max_length=85,
        required=True,
        help_text='Tipo de Evento',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    data_horas_evento = forms.DateTimeField(
        label='Selecione a data e o horario do Evento',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',  # Exibe o calendário com horário
                'id':'id_saida',
            }
        ),
        required=True, help_text='Data e o Horario do Evento'
    )
    horario_final_evento = forms.DateTimeField(
        label='Selecione a data e o horario Final do Evento',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',  # Exibe o calendário com horário
                'id':'id_saida',
            }
        ),
        required=True, help_text='Data e o Horario do Fim Evento'
    )
    nomes_autorizados = forms.CharField(
        
        label='Nomes dos Convidados',
        required=False,  # Torna o campo opcional
        widget=forms.Textarea(
            attrs={
                'placeholder':'Escreva os nomes dos Convidados...',
            }
        )
    )
    veiculos_autorizados = forms.CharField(
        label='Placas dos Carros que estão Autorizado',
        required=False,  # Torna o campo opcional
        widget=forms.Textarea(
            attrs={
                'placeholder':'Coloque as Placas dos Carros que estão Autorizado a entra no Condominio...',
            }
        )
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = models.Eventos
        fields = (
            'local_evento', 'nome_responsavel', 'tipo_de_evento', 
            'apartamento', 'data_horas_evento', 'horario_final_evento', 
            'nomes_autorizados', 'veiculos_autorizados',
        )
class RegistrorUpadateForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Primerio Nome',
        min_length=2,
        max_length=85,
        required=True,
        help_text='Digite seu Primeiro nome.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Sobrenome.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Digite Novamente Password.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()
        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()


    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email 

        if current_email != email:

            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)

            except ValidationError as errors:
                self.add_error(
                    'password1', ValidationError(errors)
                )
        return password1