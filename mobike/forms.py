from django import forms
from .models import Cliente, Bicicleta, Arriendo
from django.contrib.auth.models import User


class formularioCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
        'RUT',
        'NOMBRE_COMPLETO',
        'EDAD',
        'MEDIO_PAGO',
        'NUMERO_CELULAR',
        'EMAIL'
        ]



class formularioArriendo(forms.ModelForm):

    class Meta:
        model = Arriendo
        fields = [
        'ID_ARRIENDO',
        'CODIGO_ARRIENDO',
        'HORA_REGISTRO',
        'ID_MOBIKE',
        'ID_CLIENTE'
        ]
