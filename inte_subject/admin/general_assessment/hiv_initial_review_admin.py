from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ...admin_site import inte_subject_admin
from ...forms import HivInitialReviewForm
from ...models import HivInitialReview
from ..modeladmin import CrfModelAdminMixin


@admin.register(HivInitialReview, site=inte_subject_admin)
class HivInitialReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = HivInitialReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Diagnosis and Treatment",
            {
                "fields": (
                    "diagnosis_date",
                    "diagnosis_date_estimated",
                    "on_treatment",
                    "treatment",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    filter_horizontal = ("treatment",)

    radio_fields = {
        "diagnosis_date_estimated": admin.VERTICAL,
        "on_treatment": admin.VERTICAL,
    }
