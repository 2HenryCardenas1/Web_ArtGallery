from django import forms
from appArtGallery.models import Pieza


class Update(forms.ModelForm):
    class Meta:
        model = Pieza
        fields = [
            'nombre_pieza',
            'precio',
            'small_descripcion',
            'big_descripcion',
            'imagen',
            'imagen2',
            'imagen4'
        ]

        widgets = {
            'nombre_pieza': forms.TextInput(attrs={'class': 'form-control', 'max': '50'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'small_descripcion': forms.Textarea(
                attrs={'class': 'form-control', 'minlength': '100', 'maxlength': '250', 'rows': '3', 'max': '115',
                       'required': ''}),
            'big_descripcion': forms.Textarea(
                attrs={'class': 'form-control', 'minlength': '100', 'maxlength': '250', 'rows': '3', 'max': '255',
                       'required': ''}),
            'imagen': forms.TextInput(attrs={'class': 'form-control', 'max': '255', 'required': ''}),
            'imagen2': forms.TextInput(attrs={'class': 'form-control', 'max': '255'}),


        }
