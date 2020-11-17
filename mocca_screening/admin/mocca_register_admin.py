from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_model_admin import (
    ModelAdminFormInstructionsMixin,
    TabularInlineMixin,
    TemplatesModelAdminMixin,
)
from edc_model_admin.model_admin_simple_history import SimpleHistoryAdmin
from edc_sites import get_current_country

from ..admin_site import mocca_screening_admin
from ..forms import MoccaRegisterForm, MoccaRegisterContactForm
from ..models import MoccaRegister, MoccaRegisterContact


class MoccaRegisterContactInline(TabularInlineMixin, admin.TabularInline):

    model = MoccaRegisterContact
    form = MoccaRegisterContactForm
    min_num = 3
    # insert_after = "comment"

    # def get_formset(self, request, obj=None, **kwargs):
    #     formset = super().get_formset(request, obj=None, **kwargs)
    #     formset.validate_min = True
    #     return formset


@admin.register(MoccaRegister, site=mocca_screening_admin)
class MoccaRegisterAdmin(
    TemplatesModelAdminMixin, ModelAdminFormInstructionsMixin, SimpleHistoryAdmin
):
    form = MoccaRegisterForm
    show_object_tools = True

    # inlines = [MoccaRegisterContacts]

    fieldsets = (
        [
            "Original Enrollment Data",
            {
                "fields": (
                    "mocca_screening_identifier",
                    "mocca_study_identifier",
                    "mocca_country",
                    "mocca_site",
                    "first_name",
                    "last_name",
                    "initials",
                    "gender",
                    "age_in_years",
                    "dob",
                )
            },
        ],
        # [
        #     "Additional information",
        #     {
        #         "fields": (
        #             "age",
        #             "gender",
        #             "hiv_file_number",
        #             "hospital_number",
        #             "other_identifier",
        #         )
        #     },
        # ],
        # [
        #     "Contact information",
        #     {
        #         "fields": (
        #             "mobile_one",
        #             "mobile_one_comment",
        #             "mobile_two",
        #             "mobile_two_comment",
        #             "mobile_three",
        #             "mobile_three_comment",
        #             "comment",
        #         )
        #     },
        # ],
        audit_fieldset_tuple,
    )

    list_display = (
        "mocca_study_identifier",
        "mocca_country",
        "mocca_site",
    )

    list_filter = ("mocca_country", "mocca_site", "created", "modified")

    radio_fields = {
        "gender": admin.VERTICAL,
        "mocca_country": admin.VERTICAL,
        "mocca_site": admin.VERTICAL,
    }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "mocca_country":
            try:
                country = get_current_country()
            except AttributeError:
                country = None
            kwargs["queryset"] = db_field.related_model.objects.filter(
                mocca_country=country
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
