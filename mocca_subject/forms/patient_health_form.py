from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import PatientHealth
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
)


class PatientHealthFormValidator(CrfFormValidatorMixin, FormValidator):
    pass


class PatientHealthForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = PatientHealthFormValidator

    class Meta:
        model = PatientHealth
        fields = "__all__"
