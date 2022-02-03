from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin

from ..admin_site import mocca_subject_admin
from ..models import ArvRegimens


@admin.register(ArvRegimens, site=mocca_subject_admin)
class ArvRegimensAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass
