from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from edc_model.widgets import SliderWidget
from respond_model.form_validators_mixins import (
    CrfFormValidatorMixin,
    MedicationAdherenceFormValidatorMixin,
)

from ..models import HivMedicationAdherence


class HivMedicationAdherenceFormValidator(
    MedicationAdherenceFormValidatorMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    pass


class HivMedicationAdherenceForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HivMedicationAdherenceFormValidator

    visual_score_slider = forms.CharField(
        label="Visual Score", widget=SliderWidget(attrs={"min": 0, "max": 100})
    )

    class Meta:
        model = HivMedicationAdherence
        fields = "__all__"
