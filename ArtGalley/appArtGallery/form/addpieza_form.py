from django import forms
from appArtGallery.models import Pieza


class AddPieza(forms.ModelForm):
    class Meta:
        model = Pieza
        ordering = ['id']
        fields = [
            'nombre_pieza',
            'precio',
            'artista',
            'categoria',
            'small_descripcion',
            'big_descripcion',
            'imagen',
            'imagen2',
            'imagen4'
        ]

        widgets = {
            'nombre_pieza': forms.TextInput(attrs={'class': 'form-control', 'max': '50'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'artista': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),

            'small_descripcion': forms.Textarea(
                attrs={'class': 'form-control', 'minlength': '389', 'maxlength': '389', 'rows': '3', 'max': '115',
                       'required': ''}),
            'big_descripcion': forms.Textarea(
                attrs={'class': 'form-control', 'minlength': '300', 'maxlength': '546', 'rows': '3', 'max': '255',
                       'required': ''}),
            'imagen': forms.TextInput(attrs={'class': 'form-control', 'max': '255', 'required': ''}),
            'imagen2': forms.TextInput(attrs={'class': 'form-control', 'max': '255'}),



        }
