from django import forms
from appArtGallery.models import Artista


class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista

        fields = [
            'nombre',
            'descripcion',
            'email'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'max': '50'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'form-control', 'minlength': '700', 'maxlength': '1036', 'rows': '8'
                       }),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
        }
