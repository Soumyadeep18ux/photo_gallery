from django import forms
from .models import Photo


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']
        widgets={
        'description':forms.Textarea(attrs={
            'class':'custom-textarea',
            'placeholder':'Enter image description...',
            'rows': 2,
            

        }),
        }
