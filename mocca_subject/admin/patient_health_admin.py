from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mocca_subject_admin
from ..forms import PatientHealthForm
from ..models import PatientHealth
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(PatientHealth, site=mocca_subject_admin)
class PatientHealthAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = PatientHealthForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "PHQ-9",
            {
                "fields": (
                    "ph9interst",
                    "ph9feel",
                    "ph9troubl",
                    "ph9tired",
                    "ph9appetit",
                    "ph9badabt",
                    "ph9concen",
                    "ph9moving",
                    "phpthough",
                    "ph9functio",
                )
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "ph9interst": admin.VERTICAL,
        "ph9feel": admin.VERTICAL,
        "ph9troubl": admin.VERTICAL,
        "ph9tired": admin.VERTICAL,
        "ph9appetit": admin.VERTICAL,
        "ph9badabt": admin.VERTICAL,
        "ph9concen": admin.VERTICAL,
        "ph9moving": admin.VERTICAL,
        "phpthough": admin.VERTICAL,
        "ph9functio": admin.VERTICAL,
    }
