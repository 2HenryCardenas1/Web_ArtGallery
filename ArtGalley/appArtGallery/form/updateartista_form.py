from django import forms
from appArtGallery.models import Artista


class UpdateArtista(forms.ModelForm):
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
                attrs={'class': 'form-control', 'minlength': '50', 'maxlength': '215', 'rows': '3', 'max': '215',
                       }),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
        }
