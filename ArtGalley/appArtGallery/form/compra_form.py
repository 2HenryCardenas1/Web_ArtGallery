from django import forms
from appArtGallery.models import Facturacion


class Factura(forms.ModelForm):
    class Meta:
        model = Facturacion
        fields = [
            'nombre_usuario',
            'apellido_usuario',
            'email',
            'direccion',
            'ciudad',
            'departamento',
            'codigo_postal',
            'pieza_id_pieza'
        ]

        widgets = {
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control', 'max': '30'}),
            'apellido_usuario': forms.TextInput(attrs={'class': 'form-control', 'max': '30'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'max': '100', 'required': '', 'type': 'email'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'max': '30'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'max': '30'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control', 'max': '30'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control', 'max': '6'})


        }
