from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site
from edc_sites.models import SiteProfile


class AdminSite(DjangoAdminSite):
    site_title = "MOCCA Screening CRFs"
    site_header = "MOCCA Screening CRFs"
    index_title = "MOCCA Screening CRFs"
    site_url = "/administration/"
    enable_nav_sidebar = False  # DJ 3.1

    def each_context(self, request):
        context = super().each_context(request)
        title = SiteProfile.objects.get(site=get_current_site(request)).title
        context.update(global_site=get_current_site(request))
        label = f"MOCCA: {title.title()} - Screening CRFs"
        context.update(site_title=label, site_header=label, index_title=label)
        return context


mocca_screening_admin = AdminSite(name="mocca_screening_admin")
mocca_screening_admin.disable_action("delete_selected")
