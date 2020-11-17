from django import forms

from ..models import MoccaRegister, MoccaRegisterContact


class MoccaRegisterForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = MoccaRegister
        fields = "__all__"


class MoccaRegisterContactForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = MoccaRegisterContact
        fields = "__all__"
