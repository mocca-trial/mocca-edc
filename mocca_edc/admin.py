from django.conf import settings
from django.contrib.admin import AdminSite as DjangoAdminSite
from django.utils.translation import gettext_lazy

from .apps import AppConfig


class AdminSite(DjangoAdminSite):
    app_index_template = "edc_model_admin/admin/app_index.html"
    login_template = f"edc_auth/bootstrap{settings.EDC_BOOTSTRAP}/login.html"
    logout_template = f"edc_auth/bootstrap{settings.EDC_BOOTSTRAP}/login.html"
    enable_nav_sidebar = False  # DJ 3.1
    final_catch_all_view = True  # DJ 3.2
    site_title = gettext_lazy(AppConfig.verbose_name)

    # Text to put in each page's <h1>.
    site_header = gettext_lazy(f"{AppConfig.verbose_name}")

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy("Site administration")
    site_url = "/administration/"

    def __init__(self, **kwargs):
        super().__init__(name="mocca_edc")


mocca_edc_admin = AdminSite()
