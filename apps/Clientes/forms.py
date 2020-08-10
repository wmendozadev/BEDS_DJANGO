from django import forms

from apps.Clientes.models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = [
            'pnombre',
            'snombre',
            'pape',
            'sape',
            'direccion',
            'celular',
            'activo',
        ]

        labels = {
            'pnombre' : 'Primer nombre',
            'snombre' : 'Segundo nombre',
            'pape' : 'Primer Apellido',
            'sape' : 'Segundo Apellido',
            'direccion' : 'Direccion',
            'celular' : 'Celular',
            'activo' : 'Activo',
        }

        widgets = {
            'pnombre' :  forms.TextInput(attrs={'class':'form-control'}),
            'snombre' :  forms.TextInput(attrs={'class':'form-control'}),
            'pape' :  forms.TextInput(attrs={'class':'form-control'}),
            'sape' :  forms.TextInput(attrs={'class':'form-control'}),
            'direccion' :  forms.TextInput(attrs={'class':'form-control'}),
            'celular' :  forms.TextInput(attrs={'class':'form-control'}),
            'activo' :  forms.CheckboxInput(attrs={'class':'form-control'}),
        }