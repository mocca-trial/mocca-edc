from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from edc_visit_schedule.utils import raise_if_not_baseline
from respond_forms.form_validator_mixins import CrfFormValidatorMixin

from ..models import PatientHealth


class PatientHealthFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        raise_if_not_baseline(self.cleaned_data.get("subject_visit"))


class PatientHealthForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = PatientHealthFormValidator

    class Meta:
        model = PatientHealth
        fields = "__all__"
