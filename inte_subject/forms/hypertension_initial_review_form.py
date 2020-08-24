from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_form_validators.form_validator import FormValidator

from ..constants import DRUGS
from ..models import HypertensionInitialReview
from .mixins import (
    EstimatedDateFromAgoFormMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class HypertensionInitialReviewFormValidator(
    EstimatedDateFromAgoFormMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        self.required_if(DRUGS, field="managed_by", field_required="med_start_ago")
        if self.cleaned_data.get("med_start_ago") and self.cleaned_data.get("dx_ago"):
            if self.estimated_date_from_ago(
                "med_start_ago"
            ) < self.estimated_date_from_ago("dx_ago"):
                raise forms.ValidationError(
                    {"med_start_ago": "Invalid. Cannot be before diagnosis."}
                )


class HypertensionInitialReviewForm(
    CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm,
):
    form_validator_cls = HypertensionInitialReviewFormValidator

    class Meta:
        model = HypertensionInitialReview
        fields = "__all__"
