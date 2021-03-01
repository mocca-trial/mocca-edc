from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from respond_model.form_validators import (
    CrfFormValidatorMixin,
    GlucoseFormValidatorMixin,
    ReviewFormValidatorMixin,
)
from respond_model.utils import raise_if_clinical_review_does_not_exist

from ..models import CholReview


class CholReviewFormValidator(
    ReviewFormValidatorMixin,
    GlucoseFormValidatorMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.validate_care_delivery()
        self.validate_glucose_test()


class CholReviewForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = CholReviewFormValidator

    class Meta:
        model = CholReview
        fields = "__all__"