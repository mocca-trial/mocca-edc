from django import forms
from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import YES, NO
from edc_form_validators import FormValidator
from edc_form_validators import FormValidatorMixin
from edc_screening.modelform_mixins import AlreadyConsentedFormMixin

from ..models import SubjectScreening


class SubjectScreeningFormValidator(FormValidator):
    def clean(self):
        if (
            not self.cleaned_data.get("screening_consent")
            or self.cleaned_data.get("screening_consent") != YES
        ):
            raise forms.ValidationError(
                {
                    "screening_consent": (
                        "You may NOT screen this subject without their verbal consent."
                    )
                }
            )
        if self.cleaned_data.get("mocca_participant") != YES:
            raise forms.ValidationError(
                {
                    "mocca_participant": (
                        "Subject must have been a participant in the original MOCCA trial."
                    )
                }
            )

        self.validate_mocca_study_identifier_with_site()

        if (
            self.cleaned_data.get("age_in_years")
            and self.cleaned_data.get("age_in_years") < 18
        ):
            raise forms.ValidationError(
                {"age_in_years": "Participant must be at least 18 years old."}
            )

        self.validate_mocca_enrollment_data()

        self.required_if(
            YES, field="unsuitable_for_study", field_required="reasons_unsuitable"
        )

        self.applicable_if(
            YES, field="unsuitable_for_study", field_applicable="unsuitable_agreed"
        )

        if self.cleaned_data.get("unsuitable_agreed") == NO:
            raise forms.ValidationError(
                {
                    "unsuitable_agreed": (
                        "The study coordinator MUST agree with your assessment. "
                        "Please discuss before continuing."
                    )
                }
            )

    def validate_mocca_study_identifier_with_site(self):
        """Raises an exception if given identifier is does not exist
        for the selected site.
        """
        obj = None
        if self.cleaned_data.get("mocca_study_identifier") and self.cleaned_data.get(
            "mocca_site"
        ):
            mocca_register_cls = django_apps.get_model("mocca_screening.moccaregister")
            try:
                obj = mocca_register_cls.objects.get(
                    mocca_study_identifier=self.cleaned_data.get(
                        "mocca_study_identifier"
                    ),
                    mocca_site=self.cleaned_data.get("mocca_site"),
                )
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    {
                        "mocca_study_identifier": (
                            "Invalid MOCCA study identifier for selected site."
                        )
                    }
                )
        return obj

    def validate_mocca_enrollment_data(self):
        """Raises an exception if either the birth year or initials
        do not match the register record for the given
        `mocca_study_identifier`.
        """
        if (
            self.cleaned_data.get("mocca_study_identifier")
            and self.cleaned_data.get("mocca_site")
            and self.cleaned_data.get("birth_year")
            and self.cleaned_data.get("initials")
        ):
            mocca_register = self.validate_mocca_study_identifier_with_site()
            if mocca_register.birth_year != self.cleaned_data.get("birth_year"):
                raise forms.ValidationError(
                    {
                        "birth_year": (
                            "Invalid birth year for this MOCCA study identifier."
                        )
                    }
                )
            if mocca_register.initials != self.cleaned_data.get("initials"):
                raise forms.ValidationError(
                    {"initials": "Invalid initials for this MOCCA study identifier."}
                )


class SubjectScreeningForm(
    AlreadyConsentedFormMixin, FormValidatorMixin, forms.ModelForm
):
    form_validator_cls = SubjectScreeningFormValidator

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = SubjectScreening
        fields = [
            "screening_consent",
            "report_datetime",
            "mocca_participant",
            "mocca_site",
            "mocca_study_identifier",
            "initials",
            "gender",
            "birth_year",
            "age_in_years",
            "unsuitable_for_study",
            "reasons_unsuitable",
            "unsuitable_agreed",
        ]
