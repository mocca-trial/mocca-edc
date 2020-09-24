from django import forms
from django.contrib.sites.models import Site
from edc_constants.constants import OTHER, STUDY_DEFINED_TIMEPOINT
from edc_form_validators import FormValidatorMixin
from edc_sites.forms import SiteModelFormMixin
from edc_visit_tracking.form_validators import VisitFormValidator
from inte_prn.icc_registered import (
    InterventionSiteNotRegistered,
    is_icc_registered_site,
)
from inte_prn.models import IntegratedCareClinicRegistration
from inte_sites.is_intervention_site import NotInterventionSite
from inte_subject.constants import INTEGRATED

from ..models import SubjectVisit


class SubjectVisitFormValidator(VisitFormValidator):
    validate_missed_visit_reason = False

    def clean(self):
        super().clean()
        self.m2m_other_specify(
            OTHER, m2m_field="clinic_services", field_other="clinic_services_other",
        )

        self.validate__clinic_services()
        self.validate__health_services()

    def validate__clinic_services(self):
        selections = self.get_m2m_selected("clinic_services")
        if (
            self.cleaned_data.get("appointment").visit_code_sequence == 0
            and STUDY_DEFINED_TIMEPOINT not in selections
        ):
            raise forms.ValidationError(
                {"clinic_services": "This is scheduled study visit."}
            )
        elif (
            self.cleaned_data.get("appointment").visit_code_sequence != 0
            and STUDY_DEFINED_TIMEPOINT in selections
        ):
            raise forms.ValidationError(
                {"clinic_services": "This is not a scheduled study visit."}
            )

    def validate__health_services(self):
        selections = self.get_m2m_selected("health_services")
        if INTEGRATED in selections:
            try:
                is_icc_registered_site(
                    report_datetime=self.cleaned_data.get("report_datetime")
                )
            except NotInterventionSite:
                raise forms.ValidationError(
                    {
                        "health_services": "This site does not have an integrated care clinic."
                    }
                )
            except InterventionSiteNotRegistered as e:
                raise forms.ValidationError(
                    {
                        "health_services": (
                            "Integrated Care Clinic not "
                            "open at the time of this report. See facility form "
                            f"`{IntegratedCareClinicRegistration._meta.verbose_name}`."
                        )
                    }
                )
        self.m2m_single_selection_if(INTEGRATED, m2m_field="health_services")


class SubjectVisitForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectVisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = "__all__"
