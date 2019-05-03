from django import forms
from .models import Images

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image', 'name']