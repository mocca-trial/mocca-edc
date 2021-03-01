from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from respond_model.form_validators import (
    CrfFormValidatorMixin,
    GlucoseFormValidatorMixin,
    ResultFormValidatorMixin,
)
from respond_model.utils import (
    raise_if_baseline,
    raise_if_clinical_review_does_not_exist,
)

from ..models import Glucose


class GlucoseFormValidator(
    ResultFormValidatorMixin,
    GlucoseFormValidatorMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    def clean(self):
        if self.cleaned_data.get("subject_visit"):
            raise_if_baseline(self.cleaned_data.get("subject_visit"))
            raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.validate_drawn_date_by_dx_date(
            "dm_dx_date", "Diabetes", drawn_date_fld="glucose_date"
        )
        self.validate_glucose_test()


class GlucoseForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = GlucoseFormValidator

    class Meta:
        model = Glucose
        fields = "__all__"
