from django.contrib import admin
from edc_blood_results.fieldsets import BloodResultFieldset
from edc_model_admin import audit_fieldset_tuple

from ...admin_site import mocca_subject_admin
from ...forms import BloodResultsLipidForm
from ...models import BloodResultsLipid
from ..modeladmin_mixins import CrfModelAdmin
from .blood_results_modeladmin_mixin import (
    BloodResultsModelAdminMixin,
    conclusion_fieldset,
    summary_fieldset,
)


# TODO: Review, and verify!
@admin.register(BloodResultsLipid, site=mocca_subject_admin)
class BloodResultsLipidAdmin(BloodResultsModelAdminMixin, CrfModelAdmin):

    form = BloodResultsLipidForm

    # autocomplete_fields = ["lipid_requisition"]

    fieldsets = BloodResultFieldset(
        BloodResultsLipid.lab_panel, model_cls=BloodResultsLipid
    ).fieldsets
