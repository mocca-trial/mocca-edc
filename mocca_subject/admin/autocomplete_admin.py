from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin

from ..admin_site import mocca_subject_admin
from ..models import Rx


@admin.register(Rx, site=mocca_subject_admin)
class RxAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass
