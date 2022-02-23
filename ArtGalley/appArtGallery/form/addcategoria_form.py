from django import forms
from appArtGallery.models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre',
            'descripcion',
            'imagen'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'max': '50'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'form-control', 'minlength': '200', 'maxlength': '395', 'rows': '5', 'max': '215',
                       }),
            'imagen': forms.TextInput(attrs={'class': 'form-control', 'max': '255', 'required': ''})
        }
