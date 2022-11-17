from django import forms
from . import models

class ProfileForm(forms.ModelForm):
    pic = forms.ImageField(
        label='Profie pic',
        widget=forms.FileInput(
            attrs={'class': 'form-control bg-white border-0'}
        )
    )
    class Meta:
        model = models.Profile
        exclude = ('user', )
