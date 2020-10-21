from django.contrib import admin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_prn_admin
from ..models import EndOfStudy
from .modeladmin_mixins import EndOfStudyModelAdminMixin


@admin.register(EndOfStudy, site=inte_prn_admin)
class EndOfStudyAdmin(EndOfStudyModelAdminMixin, SimpleHistoryAdmin):

    pass
